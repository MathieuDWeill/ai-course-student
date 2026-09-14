# Windows quick fix

If setup fails on Windows, do not lose time debugging during class.

## Recommended setup

Install:

- Python 3.11 from <https://www.python.org/downloads/>
- Git for Windows from <https://git-scm.com/download/win>

During Python installation, check:

```text
Add python.exe to PATH
```

Then open **PowerShell** in the course folder.

## Commands

```powershell
git clone https://github.com/MathieuDWeill/ai-course-student.git
cd ai-course-student
.\setup.bat
.\check.bat
.\run.bat
```

Do not double-click `setup.bat`, `check.bat`, `run.bat`, or `.sh` files.

## If PowerShell blocks scripts

Use Git Bash instead:

```bash
git clone https://github.com/MathieuDWeill/ai-course-student.git
cd ai-course-student
bash setup.sh
bash check.sh
bash run.sh
```

## If Python is the problem

Check:

```powershell
py -3.11 --version
python --version
```

If neither works, reinstall Python 3.11 and check `Add python.exe to PATH`.

## Class fallback

If a machine is still blocked after 5 minutes:

1. pair with another student;
2. follow the notebook from GitHub;
3. complete the reasoning questions first;
4. fix the local environment after class.

The learning goal of S1 is not installing tools.
The learning goal is understanding why code can run and still produce a wrong result.
