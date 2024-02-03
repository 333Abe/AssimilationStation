# SQLAlchemy Models for Flashcards and Notes

## Topic Model
- Represents a high-level category.
- Attributes: `id` (primary key), `topic` (name).
- Establishes a one-to-many relationship with subtopics.

## Subtopic Model
- Represents a subcategory within a topic.
- Attributes: `id` (primary key), `subtopic` (name), `topic_id` (foreign key linking to Topic).
- Establishes one-to-many relationships with cards and notes.

## Card Model
- Represents a flashcard or question-and-answer pair.
- Attributes: `id` (primary key), `question`, `answer`, `last_answered_date`, `last_answered_correct`, `consecutive_correct`.
- Foreign key: `subtopic_id` linking to Subtopic.
- Many-to-many relationship with notes through the `card_notes_association` table.

## Note Model
- Represents a note or article.
- Attributes: `id` (primary key), `title`, `content`.
- Foreign key: `subtopic_id` linking to Subtopic.
- Many-to-many relationship with cards through the `card_notes_association` table.

## Association Table (`card_notes_association`)
- Represents a many-to-many relationship between cards and notes.
- Columns: `card_id` (foreign key linking to Card), `note_id` (foreign key linking to Note).
