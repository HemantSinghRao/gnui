// One function. That is the whole "app".
//
// `export` means: other files are allowed to use this one.
export function freeSeats(total, taken) {
  if (!Number.isInteger(total) || !Number.isInteger(taken)) {
    throw new TypeError("total and taken both have to be whole numbers");
  }
  if (total < 0 || taken < 0) {
    throw new RangeError("you cannot have a negative number of seats");
  }
  if (taken > total) {
    throw new RangeError("more seats are taken than exist");
  }
  return total - taken;
}
