// Some functions to work with the database.

// totalContribs: Returns the sum of all contributions in the database.
function totalContribs(db) {
    let result = 0;
    db['database'].forEach(user =>
        result += user['contribs']);
    return result;
}

// totalEmployees: Returns the number of Microsoft employees in the database.
function totalEmployees(db) {
    let result = 0;
    db['database'].forEach(user =>
        // Increment result if 'employed' is true.
        result += user['employed'] ? 1 : 0);
    return result;
}

// totalEmployeeContribs: Returns the sum of all Microsoft employee contributions.
function totalEmployeeContribs(db) {
    let result = 0;
    db['database'].forEach(user =>
        result += user['employed'] ? user['contribs'] : 0);
    return result;
}

// listEmployed: Returns an array of the employed status of all users.
function listEmployed(db) {
    return db['database'].map(user => user['employed']);
}

// listContribs: Returns an array of the contribution number of all users.
function listContribs(db) {
    return db['database'].map(user => user['contribs']);
}

const employeeRatio = [totalEmployees(db), db['database'].length - totalEmployees(db)];
const employeeContribRatio = [totalEmployeeContribs(db), totalContribs(db)-totalEmployeeContribs(db)];

console.log("Number of contributions: " + totalContribs(db));
console.log("Number of Microsoft employees: " + totalEmployees(db) + "/" + db['database'].length);
console.log("Number of Microsoft employee contributions: " + totalEmployeeContribs(db));
console.log(listEmployed(db));
console.log(listContribs(db));