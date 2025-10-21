// Good JavaScript examples
const goodCode1 = `
function calculateTotal(items) {
    if (!items || items.length === 0) {
        return 0;
    }
    return items.reduce((sum, item) => sum + item.price, 0);
}
`;

// Bad JavaScript examples
const badCode1 = `
function p(s){
let r=""
for(let i=0;i<s.length;i++){
r+=s[i]
}
return r
}
`;

const securityVulnerableJS = `
// XSS vulnerability
function displayUserInput() {
    const userInput = document.getElementById('userInput').value;
    document.body.innerHTML = userInput; // Dangerous innerHTML usage
}
`;