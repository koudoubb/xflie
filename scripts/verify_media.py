#!/usr/bin/env python3
"""Verify a vertical deliverable using ffprobe; optional same-size cover."""
import argparse,json,subprocess,sys

def probe(path):
 return json.loads(subprocess.check_output(['ffprobe','-v','error','-show_streams','-show_format','-of','json',path],text=True))

def main():
 ap=argparse.ArgumentParser();ap.add_argument('video');ap.add_argument('cover',nargs='?');a=ap.parse_args()
 d=probe(a.video);vs=[s for s in d['streams'] if s['codec_type']=='video'];aus=[s for s in d['streams'] if s['codec_type']=='audio'];errs=[]
 if not vs:errs.append('Missing video stream')
 else:
  v=vs[0]
  if (v['width'],v['height'])!=(1080,1920):errs.append('Expected 1080x1920')
  if v['codec_name']!='h264':errs.append('Expected H.264')
  if v.get('pix_fmt')!='yuv420p':errs.append('Expected yuv420p')
 if not aus:errs.append('Missing narration/audio stream')
 if float(d['format']['duration'])<=0:errs.append('Invalid duration')
 if int(d['format']['size'])>300*1024*1024:errs.append('File exceeds 300MiB')
 if a.cover:
  cv=next(s for s in probe(a.cover)['streams'] if s['codec_type']=='video')
  if vs and (cv['width'],cv['height'])!=(vs[0]['width'],vs[0]['height']):errs.append('Cover dimensions differ')
 print(json.dumps({'ok':not errs,'errors':errs,'duration':d['format']['duration'],'bytes':d['format']['size'],'video':[{k:s.get(k) for k in ['codec_name','width','height','pix_fmt','avg_frame_rate']} for s in vs],'audio':[{k:s.get(k) for k in ['codec_name','sample_rate','channels']} for s in aus]},ensure_ascii=False,indent=2))
 return bool(errs)
if __name__=='__main__':sys.exit(main())
