import { Client } from '@notionhq/client'
import dotenv from 'dotenv'
import axios from "axios";
import { S3 } from "./s3-client"

dotenv.config()

async function main() {
  const notionClient = new Client({ auth: process.env.NOTION_API_KEY! })

  const danses = await notionClient.databases.query({
    database_id: process.env.NOTION_DANSES_DATABASE_ID!,
    sorts: [
      {
        timestamp: "last_edited_time", // Sort by created_time
        direction: "descending",
      },
    ],
  })
  const pdfFilePropertyName = "Pdf de la chorégraphie"
  danses.results.filter(page => {
    const fileProperty = (page as any).properties[pdfFilePropertyName];
    if (!fileProperty || fileProperty.type !== "files" || fileProperty.files.length === 0) {
      return false
    }

    const notionFile = fileProperty.files[0];
    if (notionFile.type !== "file") {
      return false
    }
    return true
  }).forEach(async (page) => {
    const fileProperty = (page as any).properties[pdfFilePropertyName];
    const notionFile = fileProperty.files[0];

    const notionUrl = notionFile.file.url;
    const filename = notionFile.name || "Chorégraphie PDF.pdf";

    const response = await axios.get(notionUrl, { responseType: "arraybuffer" });
    const buffer = Buffer.from(response.data);

    const bucket = process.env.AWS_S3_BUCKET_NAME!
    const prefix = "Danses"
    const nomDeLaDanse = (page as any).properties?.Nom?.title?.[0]?.plain_text || ''
    const s3Key = `${prefix}/${nomDeLaDanse}/${filename}`

    await S3.putObject({
      Bucket: bucket,
      Key: s3Key,
      Body: buffer,
      ContentType: response.headers["content-type"] || "application/octet-stream",
    }).promise()

    const s3Url = `https://${bucket}.s3.${process.env.AWS_REGION}.amazonaws.com/${s3Key}`;

    await notionClient.pages.update({
      page_id: page.id,
      properties: {
        [pdfFilePropertyName]: {
          files: [
            {
              name: filename,
              external: { url: s3Url },
            },
          ],
        },
      },
    });

    console.log(`✅ File uploaded from Notion to S3 and updated in Notion: ${encodeURI(s3Url)}`);
    return;
  });

}

main()