import path from "path"
import fs from 'fs'
import { fileURLToPath } from 'url';
import { dirname } from 'path';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

const publicFolderPath = path.resolve(__dirname, '../public/cache')

export function saveObjectLocally(items: any[], objectRelativePublicFilePath: string) {
  const objectSaveFilePath = path.join(publicFolderPath, objectRelativePublicFilePath)

  if (!fs.existsSync(objectSaveFilePath)) {
    fs.mkdirSync(path.dirname(objectSaveFilePath), { recursive: true })
  }

  fs.writeFileSync(objectSaveFilePath, JSON.stringify(items, null, 2), 'utf-8')
  console.log(`✅ Saved: ${objectSaveFilePath}`)
}
