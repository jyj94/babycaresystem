package com.example.myapplication;

import androidx.appcompat.app.AppCompatActivity;
import androidx.constraintlayout.widget.ConstraintLayout;
import androidx.core.app.NotificationCompat;

import android.app.NotificationChannel;
import android.app.NotificationManager;
import android.content.Context;
import android.media.AudioManager;
import android.media.MediaPlayer;
import android.media.SoundPool;
import android.net.IpSecManager;
import android.os.Build;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.LinearLayout;

import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.io.PrintWriter;
import java.io.StringWriter;
import java.net.InetAddress;
import java.net.Socket;
import java.security.PublicKey;

public class MainActivity extends AppCompatActivity {

    int a;
    private SoundPool sound_pool;


    @Override
    protected void onCreate(Bundle savedInstanceState) {

        sound_pool = new SoundPool(5, AudioManager.STREAM_MUSIC, 0);
        final int sound_beep_alert = sound_pool.load(this, R.raw.baby, 1);



        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        final NotificationCompat.Builder builder = new NotificationCompat.Builder(this, "default");

        builder.setSmallIcon(R.mipmap.ic_launcher);
        builder.setContentTitle("아기한테 위험 발생");
        builder.setContentText("아기의 상태를 확인하세요.");
        final NotificationManager notificationManager = (NotificationManager) this.getSystemService(Context.NOTIFICATION_SERVICE);

        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) {
            notificationManager.createNotificationChannel(new NotificationChannel("default", "기본 채널", NotificationManager.IMPORTANCE_DEFAULT));
        }


        final ConstraintLayout back;
        back = (ConstraintLayout)findViewById(R.id.back);

        Button button2 = (Button) findViewById(R.id.button2);
        Button button = (Button) findViewById(R.id.button);

        button.setOnClickListener(new Button.OnClickListener(){
            public void onClick(View view){
                a = 1;
                back.setBackgroundResource(R.drawable.wait);

            }
        });
        button2.setOnClickListener(new Button.OnClickListener() {
            @Override
            public void onClick(View view) {
                // TODO : click event
                a = 0;
                back.setBackgroundResource(R.drawable.working);

                new Thread(new Runnable() {
                    @Override
                    public void run() {
                        String host = "aws 주소";
                        int port = 8686;

                        try{
                            Socket socket = new Socket(host, port);
                            DataOutputStream dataOutput = new DataOutputStream(socket.getOutputStream());
                            DataInputStream dataInput = new DataInputStream(socket.getInputStream());

                            dataInput.read();
                            notificationManager.notify(1, builder.build());
                            sound_pool.play(sound_beep_alert, 1f, 1f, 0, 0, 1f);



                            while(true){
                                if (a != 0)
                                    break;
                                try {
                                    Thread.sleep(100);
                                } catch (InterruptedException e) {
                                    // TODO Auto-generated catch block
                                    e.printStackTrace();
                                }
                                if (a != 0)
                                    break;
                                back.setBackgroundResource(R.drawable.warning1);try {
                                    Thread.sleep(100);
                                } catch (InterruptedException e) {
                                    // TODO Auto-generated catch block
                                    e.printStackTrace();
                                }
                                back.setBackgroundResource(R.drawable.warning2);
                                if (a != 0)
                                    break;
                            }

                        }catch (Exception e){
                            e.printStackTrace();
                        }
                    }
                }).start();
            }
        });

    }
}