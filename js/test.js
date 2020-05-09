/**
 * @param {string} s
 * @param {number} numRows
 * @return {string}
 */
var convert = function (s, numRows) {
    if (numRows === 1)
        return s;

    const a = {
        a: 1
    };
    const b = {
        a: 1
    };
    const c = [1, 2, 3, 4, 5];
    for (const t of c) {
        console.log(t);
    }
    const d = c.forEach((number, index) => {
        return number + index;
    })
    console.log(c);
    console.log(d);

    console.log(a == b);
    console.log(a === b);

    const len = Math.min(s.length, numRows);
    const rows = [];
    for (let i = 0; i < len; i++) rows[i] = "";
    let loc = 0;
    let down = false;

    for (const c of s) {
        rows[loc] += c;
        if (loc == 0 || loc == numRows - 1)
            down = !down;
        loc += down ? 1 : -1;
    }

    let ans = "";
    for (const row of rows) {
        ans += row;
    }
    return ans;
};

console.log(convert('asddddasdsadsa', 3));