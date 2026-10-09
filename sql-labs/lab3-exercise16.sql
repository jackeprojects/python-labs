-- 16. Write the CREATE TABLE statements for the music school
CREATE TABLE students (
	student_id INTEGER PRIMARY KEY,
	first_name TEXT NOT NULL,
	last_name TEXT NOT NULL
);

CREATE TABLE teachers (
	teacher_id INTEGER PRIMARY KEY,
	first_name TEXT NOT NULL,
	last_name TEXT NOT NULL
);

CREATE TABLE lessons (
	lesson_id INTEGER PRIMARY KEY,
	instrument TEXT NOT NULL,
	lesson_date TEXT NOT NULL,
	lesson_time TEXT NOT NULL,
	room INTEGER NOT NULL CHECK (room >= 0)
);

CREATE TABLE student_lessons (
	student_id INTEGER,
	lesson_id INTEGER,
	PRIMARY KEY (student_id, lesson_id),
	FOREIGN KEY (student_id) REFERENCES students (student_id),
	FOREIGN KEY (lesson_id) REFERENCES lessons (lesson_id)
);

CREATE TABLE teacher_lessons (
	teacher_id INTEGER,
	lesson_id INTEGER,
	PRIMARY KEY (teacher_id, lesson_id),
	FOREIGN KEY (teacher_id) REFERENCES teachers (teacher_id),
	FOREIGN KEY (lesson_id) REFERENCES lessons (lesson_id)
);