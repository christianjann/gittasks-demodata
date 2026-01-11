import os
import random
import datetime

base_dir = "/home/chris/data/Projects/GitTasks/gittasks-demodata"

folders = [
    "personal",
    "personal/diary",
    "personal/diary/2023",
    "personal/diary/2024",
    "personal/diary/2025",
    "personal/thoughts",
    "personal/thoughts/random",
    "personal/thoughts/inspirations",
    "personal/memories",
    "personal/memories/childhood",
    "personal/memories/adulthood",
    "personal/finances",
    "personal/finances/budget",
    "personal/finances/investments",
    "work",
    "work/meetings",
    "work/meetings/weekly",
    "work/meetings/monthly",
    "work/meetings/quarterly",
    "work/tasks",
    "work/tasks/urgent",
    "work/tasks/backlog",
    "work/tasks/completed",
    "work/projects",
    "work/projects/active",
    "work/projects/completed",
    "work/projects/proposals",
    "work/hr",
    "work/hr/policies",
    "work/hr/training",
    "projects",
    "projects/code",
    "projects/code/python",
    "projects/code/javascript",
    "projects/code/java",
    "projects/code/go",
    "projects/design",
    "projects/design/ui",
    "projects/design/ux",
    "projects/design/graphics",
    "projects/research",
    "projects/research/papers",
    "projects/research/articles",
    "projects/research/data",
    "archive",
    "archive/old_notes",
    "archive/old_notes/2019",
    "archive/old_notes/2020",
    "archive/old_notes/2021",
    "archive/backup",
    "archive/backup/2022",
    "archive/backup/2023",
    "drafts",
    "drafts/ideas",
    "drafts/ideas/tech",
    "drafts/ideas/business",
    "drafts/ideas/personal",
    "drafts/outlines",
    "drafts/outlines/books",
    "drafts/outlines/presentations",
    "drafts/outlines/reports",
    "misc",
    "misc/recipes",
    "misc/recipes/breakfast",
    "misc/recipes/dinner",
    "misc/travel",
    "misc/travel/europe",
    "misc/travel/asia",
    "misc/health",
    "misc/health/fitness",
    "misc/health/mental",
    "learning",
    "learning/courses",
    "learning/courses/online",
    "learning/courses/in_person",
    "learning/books",
    "learning/books/fiction",
    "learning/books/non_fiction",
    "learning/tutorials",
    "learning/tutorials/video",
    "learning/tutorials/text",
    "inbox",
    "inbox/quick_notes",
    "inbox/reminders",
    "inbox/emails",
    "goals",
    "goals/short_term",
    "goals/long_term",
    "goals/achievements",
    "journal",
    "journal/daily",
    "journal/weekly",
    "journal/monthly",
    "journal/yearly",
    "references",
    "references/articles",
    "references/books",
    "references/websites",
    "references/podcasts",
    "templates",
    "templates/notes",
    "templates/tasks",
    "templates/meetings",
    "templates/reports",
    "blog",
    "blog/drafts",
    "blog/published",
    "blog/ideas",
    "social",
    "social/twitter",
    "social/linkedin",
    "social/facebook",
    "events",
    "events/upcoming",
    "events/past",
    "events/birthdays",
    "shopping",
    "shopping/lists",
    "shopping/reviews",
    "hobbies",
    "hobbies/photography",
    "hobbies/gaming",
    "hobbies/reading",
    "hobbies/cooking"
]

# Create directories
for folder in folders:
    os.makedirs(os.path.join(base_dir, folder), exist_ok=True)

# Authors list
authors = ['Alice Johnson', 'Bob Smith', 'Charlie Brown', 'Diana Prince', 'Eve Adams', 'Frank Miller', 'Grace Lee', 'Henry Wilson', 'Ivy Chen', 'Jack Taylor']

# Tags pool
tag_pool = ['work', 'personal', 'urgent', 'idea', 'meeting', 'code', 'design', 'research', 'diary', 'thought', 'finance', 'health', 'learning', 'travel', 'recipe', 'goal', 'journal', 'reference', 'template', 'blog', 'social', 'event', 'shopping', 'hobby', 'task', 'note', 'draft', 'archive', 'misc']

total_files = 0
for folder in folders:
    num_files = random.randint(40, 70)  # Adjust to reach ~3000 total
    for i in range(num_files):
        filename = f"note_{i+1}.md"
        filepath = os.path.join(base_dir, folder, filename)
        
        # Generate frontmatter
        frontmatter = {}
        frontmatter['title'] = f"Note {i+1} in {folder.replace('/', ' - ')}"
        
        # Random dates
        created = datetime.datetime.now() - datetime.timedelta(days=random.randint(0, 365*3))
        updated = created + datetime.timedelta(days=random.randint(0, 365))
        frontmatter['created'] = created.isoformat()
        frontmatter['updated'] = updated.isoformat()
        
        if random.random() > 0.4:  # 60% chance
            frontmatter['source'] = f"https://example{random.randint(1,1000)}.com"
        
        if random.random() > 0.5:  # 50% chance
            frontmatter['author'] = random.choice(authors)
        
        if random.random() > 0.6:  # 40% chance
            frontmatter['latitude'] = round(random.uniform(-90, 90), 4)
            frontmatter['longitude'] = round(random.uniform(-180, 180), 4)
            frontmatter['altitude'] = random.randint(0, 5000)
        
        if random.random() > 0.4:  # 60% chance for tasks
            frontmatter['completed?'] = random.choice(['yes', 'no'])
            if random.random() > 0.5:
                due = updated + datetime.timedelta(days=random.randint(1, 365))
                frontmatter['due'] = due.isoformat()
        
        num_tags = random.randint(0, 4)
        if num_tags > 0:
            frontmatter['tags'] = random.sample(tag_pool, num_tags)
        
        # Write file
        with open(filepath, 'w') as f:
            f.write('---\n')
            for k, v in frontmatter.items():
                if k == 'tags':
                    f.write('tags:\n')
                    for tag in v:
                        f.write(f'  - {tag}\n')
                elif isinstance(v, list):
                    f.write(f'{k}: {v}\n')
                else:
                    f.write(f'{k}: {v}\n')
            f.write('---\n\n')
            f.write(f'# {frontmatter["title"]}\n\n')
            f.write('This is some sample content for the note.\n\n')
            f.write('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.\n\n')
            f.write('Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.\n')
        
        total_files += 1

print(f"Generated {total_files} notes.")