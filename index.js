import fs from "fs/promises";

let buffer = await fs.readFile("D:\\LABS\\АСД\\codes.txt");
const lines = buffer.toString().split(/\r?\n/);
let codes = lines.map(line => {
    let arr = line.split(" ");
    const symbol = String.fromCharCode(parseInt(arr[0], 16));
    const code = arr[1];
    return {symbol, code}
});

buffer = await fs.readFile("D:\\LABS\\АСД\\str.txt");
let line = buffer.toString();
let result = "";

for (let i = 0, len = 1; i < line.length; i += len, len = 1) {
    let codeFound = false;
    while (!codeFound) {
        let expectedCode = line.substring(i, i + len);
        const code = codes.find(el => el.code === expectedCode);
        if (code) {
            result += code.symbol;
            codeFound = true;
        } else len++;
    }
}
fs.writeFile("D:\\LABS\\АСД\\answer.txt", result);
console.log(result)