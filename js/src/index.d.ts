export interface SkillMeta {
  name: string
  category: 'gemini' | 'scientific' | 'claude'
  description: string
  path: string
}

export declare class Skill {
  name: string
  category: 'gemini' | 'scientific' | 'claude'
  description: string
  path: string
  prompt: string
  toString(): string
}

export declare function load(name: string, category?: 'gemini' | 'scientific' | 'claude'): Skill

export declare function search(
  query: string,
  category?: 'gemini' | 'scientific' | 'claude' | null,
  limit?: number
): SkillMeta[]

export declare function listSkills(
  category?: 'gemini' | 'scientific' | 'claude' | null
): SkillMeta[]

export declare function categories(): {
  gemini: number
  scientific: number
  claude: number
  total: number
}
