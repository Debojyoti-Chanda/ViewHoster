# Contributing to ViewHoster

Thank you for considering contributing to **ViewHoster** ! We welcome contributions in the form of bug fixes, feature enhancements, documentation improvements, and more. Please follow the steps below to ensure a smooth contribution process.

---

## Table of Contents
1. [Creating an Issue](#creating-an-issue)
2. [Discussion and Issue Assignment](#discussion-and-issue-assignment)
3. [Setting Up Your Local Environment](#setting-up-your-local-environment)
4. [Creating a New Branch](#creating-a-new-branch)
5. [Making Changes](#making-changes)
6. [Pushing Changes](#pushing-changes)
7. [Creating a Pull Request](#creating-a-pull-request)
8. [Code of Conduct](#code-of-conduct)

---

## Creating an Issue

Before starting any work, please check if the issue already exists in the [Issues](./issues) section.

1. If the issue does not exist, create a new one.
2. Include a descriptive title and detailed explanation of the issue or feature request.
3. For bugs:
   - Provide steps to reproduce the issue.
   - Mention the expected and actual behavior.
   - Add screenshots or logs if applicable.
4. Label the issue appropriately (e.g., `bug`, `enhancement`, `documentation`).

---

## Discussion and Issue Assignment

1. Wait for a project maintainer to review and respond to your issue.
2. Engage in discussions if further clarification is needed.
3. Once the issue is approved, request to have it assigned to you.

> **Note:** Work on an issue only after it has been assigned to you to avoid duplication of efforts.

---

## Setting Up Your Local Environment

1. **Fork the Repository**: 
   - Click the `Fork` button at the top-right corner of this repository to create a copy under your GitHub account.
2. **Clone the Repository**:
   ```bash
   git clone https://github.com/<your-username>/ViewHoster.git
   ```
3. **Navigate into the project directory**:
    ```bash
    cd ViewHoster
    ```
---

## Creating a New Branch

Before making changes, create a new branch. Use a naming convention like <Type>/<Describe>:

1. Branch Types:
    - bugfix/ for bug fixes.
    - feature/ for new features.

2. Create a branch:
    ```bash
    git checkout -b <Type>/<Describe>
    ```
    Example:
    ```bash
    git checkout -b bugfix/fix-login-error
    ```

---

## Making Changes
1. Make your changes in the relevant files.
2. Follow the project's coding standards and conventions.
3. Test your changes thoroughly to ensure they work as expected.

## Pushing Changes
Push your branch to your forked repository:

```bash
git push origin <branch-name>
```
Example:

```bash
git push origin bugfix/fix-login-error
```

---
## Creating a Pull Request

1. **Navigate to the original repository on GitHub.**
2. **Click New Pull Request.**
3. **Select your branch from your forked repository and compare it with the main branch of the original repository.**
4. **Add a Title and Description for your pull request:**
   * **Title:** A concise summary of the change.
   * **Description:**
     * Link the related issue (e.g., Closes #<issue-number>).
     * Describe the changes made.
     * Highlight any specific areas to review or tests added.

5. **Submit Pull Request**

---
## Code of Conduct
Please follow our Code of Conduct to maintain a welcoming and inclusive environment for everyone.