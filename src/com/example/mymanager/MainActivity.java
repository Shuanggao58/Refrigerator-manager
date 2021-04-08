package com.example.mymanager;

import android.annotation.SuppressLint;
import android.app.Activity;
import android.os.Bundle;
import android.os.Handler;
import android.os.Message;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

import java.util.HashMap;

public class MainActivity extends Activity {

    private Button btn_get_data;
    private TextView tv_data;

    @SuppressLint("HandlerLeak")
    private Handler handler = new Handler(){
        @Override
        public void handleMessage(Message msg) {

            switch (msg.what){
                case 0x11:
                    String s = (String) msg.obj;
                    tv_data.setText(s);
                    break;
                case 0x12:
                    String ss = (String) msg.obj;
                    tv_data.setText(ss);
                    break;
            }

        }
    };

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // �ؼ��ĳ�ʼ��
        btn_get_data = findViewById(R.id.btn_get_data);
        tv_data = findViewById(R.id.tv_data);

        setListener();
    }

    /**
     * ���ü���
     */
    private void setListener() {

        // ��ť����¼�
        btn_get_data.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                // ����һ���߳����������ݿⲢ��ȡ���ݿ��ж�Ӧ�������
                new Thread(new Runnable() {
                    @Override
                    public void run() {
                        // �������ݿ⹤����DBUtils��getInfoByName������ȡ���ݿ��������
                        HashMap<String, Object> map = DBUtils.getInfoByName("Charger9527");
                        Message message = handler.obtainMessage();
                        if(map != null){
                            String s = "";
                            for (String key : map.keySet()){
                                s += key + ":" + map.get(key) + "\n";
                            }
                            message.what = 0x12;
                            message.obj = s;
                        }else {
                            message.what = 0x11;
                            message.obj = "��ѯ���Ϊ��";
                        }
                        // ����Ϣ֪ͨ���̸߳���UI
                        handler.sendMessage(message);
                    }
                }).start();

            }
        });

    }
}

