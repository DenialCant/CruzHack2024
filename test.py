from flask import Flask, render_template, request, url_for, flash, redirect
from transcribe import audio_to_text
from getVideos import yt_to_mp3
import os

file_name = yt_to_mp3("testing")
        
# tran_rs = (audio_to_text(file_name))