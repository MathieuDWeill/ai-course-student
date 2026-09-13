# Student Git Workflow

Goal: work in your own copy of the course repository.

## 1. Create your copy

On GitHub, use either:

- **Use this template**: creates a clean repository under your account.
- **Fork**: creates your own fork linked to the original.

Then clone your repository:

```bash
git clone https://github.com/VOTRE-USER/ai-course-student.git
cd ai-course-student
```

## 2. Start the course environment

```bash
./setup.sh
./check.sh
./run.sh
```

Open:

```text
notebooks/01_python_data_science/B1_S01_logic_over_code.ipynb
```

## 3. Save your work

After each session:

```bash
git status
git add notebooks/ outputs/
git commit -m "Complete S1 exercises"
git push
```

## 4. What to commit

Commit:

- your edited notebooks;
- small generated outputs;
- short notes or project files.

Do not commit:

- `.venv/`;
- `.DS_Store`;
- secrets, tokens, passwords or `.env` files;
- large datasets not provided by the course.
