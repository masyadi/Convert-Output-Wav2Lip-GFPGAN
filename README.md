# Convert Output Wav2Lip-GFPGAN

Untuk convert video to image frame<br/>
`python video2image.py`

Untuk convert image frame to video<br/>
`python image2video.py`


### Wav2Lip
Untuk generate video AI<br/>
Pastikan Anda berada di directory `/Wav2Lip-GFPGAN/Wav2Lip-master` kemduan eksekusi perintah dibawah ini<br/>
`python inference.py --checkpoint_path <ckpt> --face <video.mp4> --audio <an-audio-source>`

Note:
- `<ckpt>` sesuakan dengan lokasi checkpoint model, contoh `./checkpoints/wav2lip.pth`
- `<video.mp4>` sesuaikan dengan lokasi file gambar/video Anda
- `<an-audio-source>` sesuaikan dengan lokasi file audio Anda

Lebih jelasnya bisa ke halaman ini [Link](https://github.com/Rudrabha/Wav2Lip/tree/master?tab=readme-ov-file#lip-syncing-videos-using-the-pre-trained-models-inference)


### GFPGAN
Untuk menghasilkan restorasi gambar yang tinggi<br/>
Pastikan Anda berada di directory `/Wav2Lip-GFPGAN/GFPGAN-master` kemudian eksekusi perintah dibawah ini<br/>
`python inference_gfpgan.py -i inputs/whole_imgs -o results -v 1.3 -s 2`

Note:
- `inputs/whole_imgs` sesuakan dengan directory dimana file gambar Anda berada
- `results` sesuaikan dengan directory dimana hasil generate akan disimpan

Lebih jelasnya bisa ke halaman ini [Link](https://github.com/TencentARC/GFPGAN?tab=readme-ov-file#zap-quick-inference)


### Project reference:
1. https://github.com/ajay-sainy/Wav2Lip-GFPGAN
2. https://github.com/zachysaur/Wav2lip-Gfpgan-Cpu-Installation

