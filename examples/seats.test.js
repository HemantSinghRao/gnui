// Run it with:   node --test
//
// `node:test` and `node:assert` come with Node itself. Nothing to install.
import test from "node:test";
import assert from "node:assert/strict";
import { freeSeats } from "./seats.js";

test("counts the seats nobody is sitting in", () => {
  assert.equal(freeSeats(120, 97), 23);
});

test("a full library has no free seats", () => {
  assert.equal(freeSeats(120, 120), 0);
});

test("refuses impossible numbers instead of quietly lying", () => {
  assert.throws(() => freeSeats(10, 11), RangeError);
  assert.throws(() => freeSeats("120", 97), TypeError);
});
