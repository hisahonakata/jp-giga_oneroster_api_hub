import sqlite3

connection = sqlite3.connect("oneroster.db")
cursor = connection.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS AcademicSession(sourceId text, status text, dateLastModified text title text, type text, startDate text, endDate text, parentSourcedId text, schoolYear text)")
cursor.execute("CREATE TABLE IF NOT EXISTS Class(sourceId text, status text, dateLastModified text. title text, grade text, courceSourcedId text, classCode text, classType text, location text, schoolSourcedId text, termSourcedIds text, subjects text, subjectCodes text, period text, specialNeeds text)")
cursor.execute("CREATE TABLE IF NOT EXISTS Course(sourceId text, status text, dateLastModified text, schoolYearSourcedId text, title text, courseCode text, grades text, orgSourcedId text, subjects text, subjectCodes text)")
cursor.execute("CREATE TABLE IF NOT EXISTS Demographics(sourceId text, status text, dateLastModified text, barthDate text, sex text)")
cursor.execute("CREATE TABLE IF NOT EXISTS Enrollment(sourceId text, status text, dateLastModified text, classSourcedId text, schoolSroucedId text, userSourcedId text, role text, primary text, beginDate text, endDate text, ShussekiNo text)")
cursor.execute("CREATE TABLE IF NOT EXISTS Orgs(sourceId text, status text, dateLastModified text, name text, type text, identifier text, parentSourcedId text)")
cursor.execute("CREATE TABLE IF NOT EXISTS Roles(sourceId text, status text, dateLastModified text, userSourcedId text, roleType text, beginDate text, endDate text, orgSourcedId text, userProfileSroucedId text)")
cursor.execute("CREATE TABLE IF NOT EXISTS UserProfile(sourceId text, status text, dateLastModified text, userSourcedId text, profileType text, venderId text, applicationId text, description text, credentialType text, username text, password text)")
cursor.execute("CREATE TABLE IF NOT EXISTS User(sourceId text, status text, dateLastModified text, enabledUser text, username text, userIds text, givenName text, familyName text, middleName text, identifier text, email text, sms text, phone text, agentSourcedIds text, grades text, password text, userMasterIdentifer text, resourceSourcedIds text, preferredGivenName text, preferredMiddleName text, preferredFamiliName text, primaryOrgSourcedId text, kanaGiveName text, kanaFamilyName text, kanaMiddleName text, homeClass text)")

connection.commit()
connection.close()