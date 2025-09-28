import dotenv from 'dotenv'

dotenv.config()

export class Config {
  // Notion
  static readonly NOTION_API_KEY: string = process.env.NOTION_API_KEY!;
  static readonly NOTION_DANSES_DATABASE_ID: string = process.env.NOTION_DANSES_DATABASE_ID!;
  static readonly NOTION_COURS_DATABASE_ID: string = process.env.NOTION_COURS_DATABASE_ID!;
  // AWS
  static readonly AWS_ACCESS_KEY_ID: string = process.env.AWS_ACCESS_KEY_ID!;
  static readonly AWS_SECRET_ACCESS_KEY: string = process.env.AWS_SECRET_ACCESS_KEY!;
  static readonly AWS_REGION: string = process.env.AWS_REGION!;
  static readonly AWS_S3_BUCKET_NAME: string = process.env.AWS_S3_BUCKET_NAME!;
  static readonly AWS_S3_CONFIG = {
    accessKeyId: Config.AWS_ACCESS_KEY_ID,
    secretAccessKey: Config.AWS_SECRET_ACCESS_KEY,
    region: Config.AWS_REGION,
  }
}