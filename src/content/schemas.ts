import { z } from 'zod'

export const CourSchema = z.object({
  type: z.enum(['COUNTRY']),
  niveau: z.enum(['BEGINNER', 'INTERMEDIATE', 'ADVANCED']),
  danses_revisees: z.array(z.string()),
  danse_apprise: z.array(z.string()),
  date_realisation: z.date()
});

export const DanseSchema = z.object({
  nom: z.string().min(1, { message: "Le nom de la danse est requis" }),
  lien_musique: z.string().url().nullable(),
  video_choregraphie: z.string().url().optional(),
  pdf_choregraphie: z.string().url().optional(),
});

export type Cour = z.infer<typeof CourSchema>
export type Danse = z.infer<typeof DanseSchema>