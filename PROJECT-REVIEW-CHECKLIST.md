# Project Review Checklist

## 1. Repo structure
- [x] Remove folders that are no longer meant to be public
- [x] Confirm final public folder structure is clean and intentional
- [x] Confirm no duplicate folders exist because of naming mismatches
- [x] Confirm screenshot folder naming is consistent
- [x] Confirm no empty placeholder folders remain unless truly needed

## 2. README
- [x] Project title is clear
- [x] One-line project definition is strong
- [x] Current status section is accurate
- [x] "Why Voice API instead of full telephony platform" is included
- [x] "How the API links to the 3 incidents" is included
- [x] Monitoring section is included
- [x] Repo scope/public scope is explained if needed
- [x] Screenshots in README render correctly
- [x] README does not mention removed folders or removed scope
- [x] README is readable from top to bottom without confusion

## 3. Core technical implementation
- [x] `app/api-service/app.py` is present and correct
- [x] `app/api-service/requirements.txt` is correct
- [x] `app/api-service/systemd/voice-api.service` matches working EC2 version
- [x] No incorrect hardcoded paths remain
- [x] Public repo reflects the real working version

## 4. Monitoring docs
- [ ] `monitoring/cloudwatch-alarms.md` is complete
- [ ] `monitoring/alert-scenarios.md` is complete
- [ ] Alarm names match actual CloudWatch alarms
- [ ] Monitoring docs mention what each alarm is used for
- [ ] Monitoring docs include relevant screenshots where useful

## 5. Incident 001 docs
- [ ] `incident-record.md` exists
- [ ] `triage-notes.md` exists
- [ ] `handover-note.md` exists
- [ ] `stakeholder-update.md` exists
- [ ] `PRB-001-recurring-memory-growth.md` exists
- [ ] Incident 001 text matches what actually happened
- [ ] Commands listed are accurate
- [ ] Screenshots are embedded correctly
- [ ] Jira evidence is mentioned

## 6. Incident 002 docs
- [ ] `incident-record.md` exists
- [ ] `triage-notes.md` exists
- [ ] `handover-note.md` exists
- [ ] `stakeholder-update.md` exists
- [ ] `CHG-001-security-group-correction.md` exists
- [ ] Incident 002 text matches what actually happened
- [ ] Distinction between local health and external failure is clearly explained
- [ ] Screenshots are embedded correctly
- [ ] Jira evidence is mentioned

## 7. Incident 003 docs
- [ ] `incident-record.md` exists
- [ ] `triage-notes.md` exists
- [ ] `handover-note.md` exists
- [ ] `stakeholder-update.md` exists
- [ ] Vendor/dependency escalation angle is clearly explained
- [ ] "platform up, service degraded" is clearly stated
- [ ] Simulated voice dependency logs are explained properly
- [ ] Screenshots are embedded correctly
- [ ] Jira evidence is mentioned

## 8. Jira/process/docs review
- [ ] Jira screenshots support the repo rather than overwhelm it
- [ ] There is at least one structured-delivery/Jira overview screenshot
- [ ] Incident Jira screenshots are placed in the right docs
- [ ] Documentation is consistent with the actual Jira workflow
- [ ] Change/problem/incident terminology is used consistently

## 9. Screenshot review
- [ ] Screenshot filenames are clean and consistent
- [ ] Folder names are consistent (`screenshots`, not mixed variants)
- [ ] No broken image links in markdown
- [ ] Images chosen are useful, not repetitive
- [ ] Images are placed only where they add clarity
- [ ] README uses only a few key screenshots
- [ ] Incident docs contain the deeper evidence screenshots

## 10. Final polish
- [ ] No spelling mistakes in major headings
- [ ] No outdated text remains from older scope versions
- [ ] No broken markdown links
- [ ] No private/sensitive information is exposed
- [ ] Repo description on GitHub matches the final project
- [ ] Final commit history looks clean enough
- [ ] Project reads well for a recruiter or hiring manager