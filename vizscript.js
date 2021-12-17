// Some extra functions to process the JSON database.
d3.json("db.json").then(function(db) {

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

    const employeeRatio = [totalEmployees(db), db['database'].length - totalEmployees(db)];

    console.log("Number of contributions: " + totalContribs(db));
    console.log("Number of Microsoft employees: " + totalEmployees(db) + "/" + db['database'].length);
})