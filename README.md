# GitTasks Demo Data

This repository contains test and demo data for [GitTasks](https://github.com/christianjann/gittasks), a notetaking application that uses Git as its backend.

## Overview

This demo dataset includes approximately 6,700+ markdown notes organized in a hierarchical folder structure. Each note is a standard Markdown file with YAML frontmatter containing metadata.

## Folder Structure

The notes are distributed across various folders to simulate real-world usage:

- `personal/` - Personal notes, diaries, thoughts, memories, finances
- `work/` - Work-related notes, meetings, tasks, projects, HR
- `projects/` - Project notes, code, design, research
- `archive/` - Archived old notes and backups
- `drafts/` - Draft ideas, outlines
- `misc/` - Miscellaneous notes like recipes, travel, health
- `learning/` - Courses, books, tutorials
- `inbox/` - Quick notes, reminders, emails
- `goals/` - Short-term and long-term goals
- `journal/` - Daily, weekly, monthly journals
- `references/` - Articles, books, websites, podcasts
- `templates/` - Note templates
- `blog/` - Blog drafts and published posts
- `social/` - Social media notes
- `events/` - Upcoming and past events
- `shopping/` - Shopping lists and reviews
- `hobbies/` - Photography, gaming, reading, cooking
- `examples/` - Original example notes

Folders have varying depths (1-4 levels) to test hierarchical organization.

## Frontmatter Fields

Each note uses YAML frontmatter with the following supported fields:

- `title`: Title of the note
- `updated`: Last update timestamp (ISO format)
- `created`: Creation timestamp (ISO format)
- `source`: Source URL (if applicable)
- `author`: Author's name
- `latitude`: Latitude coordinate
- `longitude`: Longitude coordinate
- `altitude`: Altitude in meters
- `completed`: Boolean indicating if a task is completed
- `due`: Due date for tasks (ISO format)
- `tags`: List of associated tags (multi-line YAML format)

## Usage

This data can be used for:

- Testing GitTasks functionality
- Benchmarking performance with large datasets
- Demonstrating features like search, filtering, and organization
- Development and debugging

## Generation

The notes were generated using a Python script (`generate_notes.py`) that creates randomized content with varied frontmatter to simulate realistic usage patterns.

## License

This demo data is provided for testing purposes. See the main [GitTasks repository](https://github.com/christianjann/gittasks) for licensing information.