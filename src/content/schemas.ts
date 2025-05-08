import { z } from 'zod'

export const NiveauxDesCours = z.enum(['Débutant', 'Intermédiaire', 'Avancé'])

export const CoursSchema = z.object({
  niveau: NiveauxDesCours,
  danses_revisees: z.array(z.string()),
  danses_apprises: z.array(z.string()),
  date_realisation: z.date()
});

export const DanseSchema = z.object({
  nom: z.string().min(1, { message: "Le nom de la danse est requis" }),
  lien_musique: z.string().url().optional(),
  lien_video_choregraphie: z.string().url().optional(),
  lien_pdf_choregraphie: z.string().url().optional(),
});
