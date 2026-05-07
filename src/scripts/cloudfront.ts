import { Config } from './config'

export function s3KeyToCloudFrontUrl(s3Key: string): string {
  const encodedPath = s3Key.split('/').map(segment => encodeURIComponent(segment)).join('/')
  return `https://${Config.CLOUDFRONT_HOST}/${encodedPath}`
}

export function s3UrlToCloudFrontUrl(s3Url: string): string {
  const url = new URL(s3Url)
  const path = url.pathname.replace(/\+/g, '%20')
  return `https://${Config.CLOUDFRONT_HOST}${path}`
}

export function isS3Url(url: string): boolean {
  return url.includes('.amazonaws.com')
}
