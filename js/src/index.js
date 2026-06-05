'use strict'

const fs = require('fs')
const path = require('path')

const INDEX_PATH = path.join(__dirname, '..', 'index.json')
const SKILLS_ROOT = path.join(__dirname, '..', 'skills')

let _index = null

function getIndex() {
  if (!_index) {
    _index = JSON.parse(fs.readFileSync(INDEX_PATH, 'utf-8'))
  }
  return _index
}

class Skill {
  constructor(meta, content) {
    this.name = meta.name
    this.category = meta.category
    this.description = meta.description
    this.path = meta.path
    this.prompt = content
  }

  toString() {
    return this.prompt
  }
}

/**
 * Load a skill by name. Reads from disk only when called.
 * @param {string} name - Skill name
 * @param {string} [category] - Optional: "gemini" | "scientific" | "claude"
 * @returns {Skill}
 * @example
 * const skill = load('scientific-brainstorming')
 * console.log(skill.prompt)
 */
function load(name, category = null) {
  const index = getIndex()
  const matches = index.skills.filter(
    s => s.name === name && (category === null || s.category === category)
  )

  if (matches.length === 0) {
    throw new Error(
      `Skill '${name}' not found. Use search('${name}') to find similar skills.`
    )
  }

  if (matches.length > 1 && category === null) {
    const cats = matches.map(m => m.category)
    throw new Error(
      `Skill '${name}' exists in multiple categories: ${cats.join(', ')}. ` +
      `Specify category, e.g. load('${name}', '${cats[0]}')`
    )
  }

  const meta = matches[0]
  const relPath = meta.path.replace(/^skills\//, '')
  const skillPath = path.join(SKILLS_ROOT, ...relPath.split('/'))
  const content = fs.readFileSync(skillPath, 'utf-8')
  return new Skill(meta, content)
}

/**
 * Search skills by keyword in name or description.
 * @param {string} query
 * @param {string} [category]
 * @param {number} [limit=10]
 * @returns {Array<{name: string, category: string, description: string}>}
 */
function search(query, category = null, limit = 10) {
  const index = getIndex()
  const q = query.toLowerCase()
  return index.skills
    .filter(s =>
      (s.name.toLowerCase().includes(q) || s.description.toLowerCase().includes(q)) &&
      (category === null || s.category === category)
    )
    .slice(0, limit)
    .map(s => ({ name: s.name, category: s.category, description: s.description }))
}

/**
 * List all skills, optionally filtered by category.
 * @param {string} [category]
 * @returns {Array<{name: string, category: string, description: string}>}
 */
function listSkills(category = null) {
  const index = getIndex()
  return index.skills
    .filter(s => category === null || s.category === category)
    .map(s => ({ name: s.name, category: s.category, description: s.description }))
}

/**
 * Return skill counts per category.
 * @returns {{gemini: number, scientific: number, claude: number, total: number}}
 */
function categories() {
  const index = getIndex()
  const counts = {}
  for (const s of index.skills) {
    counts[s.category] = (counts[s.category] || 0) + 1
  }
  counts.total = index.total
  return counts
}

module.exports = { load, search, listSkills, categories, Skill }
