import { saveObjectLocally } from './save-object-locally'
import { Config } from "./config"
import AWS from 'aws-sdk'


async function main() {
  const S3 = new AWS.S3(Config.AWS_S3_CONFIG)

  const bucket = Config.AWS_S3_BUCKET_NAME
  const prefix = 'Albums photos/'

  const folders = await S3.listObjectsV2({
    Bucket: bucket,
    Prefix: prefix,
    Delimiter: '/',
  }).promise()

  const albums = []
  for (const commonPrefix of folders.CommonPrefixes || []) {
    const folderPath = commonPrefix.Prefix!  // e.g. "Albums photos/2018-10-20 Santa Suzanna/"

    // Extract folder name without the main prefix and trailing slash
    const folderName = folderPath.slice(prefix.length, -1)  // "2018-10-20 Santa Suzanna"

    // Parse date and name (assuming first 10 chars is date)
    const date = folderName.slice(0, 10)   // "2018-10-20"
    const name = folderName.slice(11)      // "Santa Suzanna"

    // List photos inside this folder
    const photosResp = await S3.listObjectsV2({
      Bucket: bucket,
      Prefix: folderPath,
    }).promise()

    const photos = photosResp.Contents?.map(obj => {
      return `https://${bucket}.s3.amazonaws.com/${obj.Key}`
    }) ?? []

    albums.push({
      id: folderName,
      date,
      name,
      photos,
    })
  }

  saveObjectLocally(albums, "albums.json")
}

main()