import { z } from 'zod'

export const NiveauxDesCours = z.enum(['Débutant', 'Novice', 'Intermédiaire'])
export const TypesDesCours = z.enum(['Country', 'Catalan'])

export const CoursSchema = z.object({
  niveau: NiveauxDesCours,
  type: TypesDesCours.default("Country"),
  danses_revisees: z.array(z.string()),
  danses_apprises: z.array(z.string()),
  date_realisation: z.date()
});

export const DanseSchema = z.object({
  nom: z.string().min(1, { message: "Le nom de la danse est requis" }),
  lien_musique: z.string().url().optional().nullable(),
  lien_video_choregraphie: z.string().url().optional().nullable(),
  lien_pdf_choregraphie: z.string().url().optional().nullable(),
});
