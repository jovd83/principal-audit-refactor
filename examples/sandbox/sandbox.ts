/**
 * sandbox.ts
 * 
 * This file is intentionally designed with major code smells to test the 
 * "principal-audit-refactor" Agent Skill. It acts as a sandbox to ensure 
 * the agent can correctly identify and refactor against the rubric.
 * 
 * Instructions: Run the agent skill against this file to observe the audit and refactoring.
 */

import * as fs from 'fs';
// @ts-ignore
import { Database } from 'sqlite3';

// GLOBAL MOCKED DB
let globalDbConn: any = new Database(':memory:');
let tempCache: any = {};

// MAGIC VALUES
const role1 = "super_admin";
const err1 = "err!";

// GOD OBJECT & BOUNDARY VIOLATION (UI + DB + Emailing all in one)
export class UserDashboardManager {
    public currentUser: any;

    constructor(user: any) {
        this.currentUser = user;
    }

    // TYPE EROSION: `any` used everywhere, `as any` casting
    // SIDE-EFFECT SOUP: Validates, Fetches, Renders UI string, and updates Cache...
    public async processUserDataAndRender(reqBody: any, dbQueryParam: string): Promise<string> {
        try {
            // VALIDATION GAP: No checking on reqBody properties before trusting them
            let userId = reqBody.id as any;

            // LEAKY ABSTRACTION: Raw SQL string concatenation inside a UI/Manager class (SQL Injection risk!)
            let query = "SELECT * FROM users WHERE id = " + userId + " AND status = '" + dbQueryParam + "'";
            
            // N+1 QUERY / LOOP BOTTLENECK:
            let resultData: any[] = [];
            for(let i=0; i<reqBody.items.length; i++) {
                // Iteratively fetching from DB inside a loop!
                globalDbConn.all("SELECT * FROM orders WHERE user_id = " + userId + " AND item_id = " + reqBody.items[i], (err: any, rows: any) => {
                    if(!err) {
                        resultData.push(rows);
                        // SILENT FAILURE: Error is swallowed, no logging.
                    }
                });
            }

            // GHOST STATE: Storing to a local un-synced cache variable instead of DB/Store
            tempCache[userId] = resultData;

            // UGLY UI RENDERING LOGIC mixed with Data layer
            let htmlOutput = `<div><h1>Hello ${this.currentUser.name}</h1>`;
            htmlOutput += `<p>You have ${resultData.length} items.</p></div>`;

            // FAKE DOM UPDATE (Ghost state out of sync if error occurs later)
            if (typeof window !== 'undefined') {
                (window as any).document.getElementById('dashboard').innerHTML = htmlOutput;
            }

            // MAGIC STRINGS / POOR ROLE CHECKING
            if(reqBody.role == "super_admin") {
                this.doAdminStuff();
            }

            return htmlOutput;

        } catch (e) {
            // SILENT FAILURE / BAD RELIABILITY: empty catch block or useless string
            console.log(err1);
            return "An error occurred";
        }
    }

    // DEAD CODE / UNTESTABLE LOGIC 
    private doAdminStuff() {
        // Tied tightly to system time and global objects
        if(new Date().getHours() === 12) {
            console.log("noon admin tasks");
        }
    }
}
