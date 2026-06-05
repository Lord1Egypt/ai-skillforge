#!/usr/bin/env node
'use strict'

const { load, search, listSkills, categories } = require('../src/index')

const [,, command, ...args] = process.argv

function help() {
  console.log(`
skillforge-agent CLI — 1,026 lazy-loading AI skills

Usage:
  skillforge load <name> [--category <cat>]   Load and print a skill
  skillforge search <query> [--category <cat>] Search skills
  skillforge list [--category <cat>]           List all skills
  skillforge stats                             Show counts per category

Categories: gemini, scientific, claude
`)
}

function getOpt(args, flag) {
  const i = args.indexOf(flag)
  return i !== -1 ? args[i + 1] : null
}

if (!command || command === '--help' || command === '-h') {
  help()
  process.exit(0)
}

if (command === 'load') {
  const name = args[0]
  if (!name) { console.error('Usage: skillforge load <name>'); process.exit(1) }
  const category = getOpt(args, '--category') || getOpt(args, '-c')
  try {
    const skill = load(name, category)
    console.log(`# ${skill.name} [${skill.category}]\n`)
    console.log(skill.prompt)
  } catch (e) {
    console.error('Error:', e.message)
    process.exit(1)
  }
}

else if (command === 'search') {
  const query = args[0]
  if (!query) { console.error('Usage: skillforge search <query>'); process.exit(1) }
  const category = getOpt(args, '--category') || getOpt(args, '-c')
  const limitArg = getOpt(args, '--limit') || getOpt(args, '-n')
  const limit = limitArg ? parseInt(limitArg) : 10
  const results = search(query, category, limit)
  if (!results.length) {
    console.log(`No skills found for '${query}'`)
  } else {
    for (const r of results) {
      console.log(`[${r.category.padEnd(12)}] ${r.name}`)
      if (r.description) console.log(`               ${r.description.slice(0, 80)}...`)
      console.log()
    }
  }
}

else if (command === 'list') {
  const category = getOpt(args, '--category') || getOpt(args, '-c')
  const skills = listSkills(category)
  for (const s of skills) {
    console.log(`[${s.category.padEnd(12)}] ${s.name}`)
  }
}

else if (command === 'stats') {
  const stats = categories()
  for (const [k, v] of Object.entries(stats)) {
    console.log(`  ${k.padEnd(15)} ${v}`)
  }
}

else {
  console.error(`Unknown command: ${command}`)
  help()
  process.exit(1)
}
