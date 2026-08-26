# Course extraction algorithm

Goal: turn a video course URL into structured source material for the website without leaking API keys or losing provenance.

## Pipeline

1. Identify the source
   - Normalize YouTube URLs to a canonical video id.
   - Store source metadata in `extracted_courses/<video_id>/metadata.json`.

2. Extract raw material
   - Prefer official/available captions through `yt-dlp`.
   - Save captions as VTT and a cleaned transcript as JSONL plus Markdown.
   - If captions are unavailable, download audio for later transcription.

3. Normalize
   - Split transcript into time-window chunks.
   - Preserve timestamps, source URL, language, and extraction method.
   - Build a raw manifest so every generated paragraph can point back to the source.

4. Enrich with APIs
   - Gemini first, because the existing site already uses it.
   - OpenRouter second for alternate model synthesis.
   - DeepSeek third for inexpensive text-only refinement.
   - Anthropic can be added later for a stricter pedagogical review pass.

5. Generate web-ready artifacts
   - `course_outline.json`: modules, lessons, concepts, exercises, glossary.
   - `site_content.json`: copy blocks directly consumable by the frontend.
   - `course_notes.md`: readable notes for teacher review.
   - `extraction_report.md`: what was extracted, what failed, and what needs manual review.

6. Human review before publishing
   - Check factual accuracy against the transcript.
   - Remove copyrighted long-form transcript from the public site.
   - Publish summaries, lesson structures, short attributed excerpts, exercises, and original commentary.

## Batch automation

Create a UTF-8 text file with one YouTube URL or video id per line. Blank lines
and lines beginning with `#` are ignored.

```powershell
python tools/publish_course.py --urls-file clases.txt --provider auto
```

The command extracts and enriches every class, then rebuilds the website JSON
once. After reviewing the generated material, publish only those class outputs:

```powershell
python tools/publish_course.py --urls-file clases.txt --provider auto --deploy
```

Automatic deployment refuses to run outside `main`, when files are already
staged, or when any Git step fails. It never uses `git add -A`.

## Copyright boundary

The website should not republish a full transcript or large verbatim sections from the video. The extractor keeps the full transcript locally for analysis, then generates summaries, lesson plans, exercises, glossary entries, and short cited snippets.
