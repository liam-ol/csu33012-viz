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

// listProps: Returns an array of a given property of all database entries.
function listProps(db, property) {
    return db['database'].map(user => user[property]);
}

const employeeRatio = [totalEmployees(db), db['database'].length - totalEmployees(db)];
const employeeContribRatio = [totalEmployeeContribs(db), totalContribs(db)-totalEmployeeContribs(db)];
const listNames = listProps(db,'name');
const listEmployed = listProps(db,'employed');
const listContribs = listProps(db,'contribs');

const microsoftPercent = (totalEmployees(db) / db['database'].length * 100).toPrecision(3);
const contribPercent = (totalEmployeeContribs(db) / totalContribs(db) * 100).toPrecision(3);

console.log("Number of contributions: " + totalContribs(db));
console.log("Number of Microsoft employees: " + totalEmployees(db) + "/" + db['database'].length);
console.log("Number of Microsoft employee contributions: " + totalEmployeeContribs(db));
console.log(listProps(db,'employed'));
console.log(listProps(db,'contribs'));