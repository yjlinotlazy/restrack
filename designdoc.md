# ResTrack Design Doc

## Use Cases
User can use_ResTrack_ to track progress against resolution project
objectives. It allows user to
 - Create projects
 - Under each goal, customize tasks to be tracked
 - For each task, customize numbers to be recorded as progress
 - Define progress tracking by simple arithmetic operations
 - View report

### User Interfaces

**Main Menu**
 - View existing list of projects
 - View reports
 - Create New projects
 - Configuration

**Project**
 - View existing list of tasks
 - Add new tasks
 - Go back to main menu

**Task**
 - Log progress
   - Enter timestamp (defaults to today's date)
   - Enter numbers (display user defined formula)
   - Back to project when done above
 - Back to project
 - View the most recent five logs

**Task Creation**
  - Create task
    - Define variables to log
    - Define aggregated number for KPI

**Customize Progress**
  - Create KPI

**Reports**
 - Plot KPI over time

**Configuration**
 - Location of config file (default is `~/.restrack/config.json`)
 - Location of data file (default is `~/.restrack/db.csv`)
