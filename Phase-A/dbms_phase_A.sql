
create table courseCatalogue
(
    courseID varchar(10),
    L int,
    T int,
    P int,
    S int,
    C int
);
alter table courseCatalogue
	add constraint coursecatalogue_pk
		primary key (courseID);


create table prerequisite
(
	"courseID" varchar(10) not null
		constraint prerequisite_coursecatalogue_courseid_fk
			references courseCatalogue (courseID),
	"prerequisiteCourseID" varchar(10) not null
);


create table "courseOffering"
(
	"courseID" varchar(10) not null,
	semester int not null,
	year int not null,
	"minCGPA" numeric(2,2) default 0,
	teacherID varchar(10),
	section int,
	"timeSlotID" int
);

alter table "courseOffering"
	add constraint """courseoffering""_pk"
		primary key ("courseID","section","semester","year");

create trigger afterCourseOffered
    after insert
    on "courseOffering"
execute procedure createEligibleBatchesAndBranches();






create table "timeSlots"
(
	id serial,
	"startTime" char(5) not null,
	"endTime" char(5) not null
);

comment on table "timeSlots" is 'start time and end time are in 24 hour format. For example: 09.05';

create unique index timeslots_id_index
	on "timeSlots" (id);

alter table "timeSlots"
	add constraint timeslots_pk
		primary key (id);



create table teacher
(
	"teacherID" varchar(30),
	name varchar(30),
	department varchar(30)
);
alter table teacher alter column "teacherID" set not null;



create unique index teacher_teacherID_index
	on teacher ("teacherID");

alter table teacher
	add constraint teacher_pk
		primary key ("teacherID");


create table offers
(
	"courseID" varchar(10),
	teacherID varchar(30),
	"timeSlotID" int,
	semester int,
	year int,
	section int
);

comment on table offers is 'offers is a multiway relation between courseCatalogue, timeSlots, teacher and courseOffering';


create table "studentRecord"
(
	"studentID" char(11) not null,
	name varchar(30),
	batch int,
	branch char(3),
	"programCoreCredits" int default 0,
	"programElectiveCredits" int default 0,
	"openElectiveCredits" int default 0,
	"scienceCoreCredits" int default 0
);

create unique index studentRecord_studentID_index
	on "studentRecord" ("studentID");

alter table "studentRecord"
	add constraint studentRecord_pk
		primary key ("studentID");

create table takes
(
	"studentID" char(11),
	"courseID" varchar(10),
	semester int,
	year int
);

create unique index takes_studentID_index
	on takes ("studentID");

create or replace function createEligibleBatchesAndBranches() returns trigger
as
$$
declare
    courseID "courseOffering"."courseID"%type := NEW."courseID";
    semester int := NEW.semester;
    year int := NEW.year;
    eligibleID varchar(50):= courseID || semester || year;
begin
    execute format('create table if not exists %I','batch' || eligibleID);
    execute format('create table if not exists %I','branch' || eligibleID);
end;
$$
 language plpgsql;
