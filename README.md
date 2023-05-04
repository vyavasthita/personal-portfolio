# personal-portfolio
Personal Portfolio

# Schema
Company
	name
	address
	duration (start and end date/present)
	designation

Technology
	name
	type

Expertise
	level
	value

Skill
	experience
	expertise_level (FK of Expertise)
	technology (FK)

Projects
	name
	duration
	role
	designation
	technologies used
	Company id (FK)

Institution
	name
	address
	type (Private, Govt, Trust)
	affiliated by
	university


Education
	details - FK of Institution
	duration
	specialization


Profile
	name
	dob
	add
	email
	phone
	about me
