package com.example.mymanager;

import android.content.Context;
import android.util.Log;
import android.widget.Toast;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.HashMap;

/**
 * ���ݿ⹤���ࣺ�������ݿ��á���ȡ���ݿ�������
 * ��ز������ݿ�ķ�������д�ڸ���
 */
public class DBUtils {

    private static String driver = "com.mysql.jdbc.Driver";// MySql����

//    private static String url = "jdbc:mysql://localhost:3306/map_designer_test_db";

    private static String user = "root";// �û���

    private static String password = "123456";// ����

    private static Connection getConn(String dbName){

        Connection connection = null;
        try{
            Class.forName(driver);// ��̬������
            String ip = "192.168.3.61";// д�ɱ�����ַ������д��localhost��ͬʱ�ֻ��͵������ӵ����������ͬһ��

            // ���Խ������������ݿ�URL������
            connection = DriverManager.getConnection("jdbc:mysql://" + ip + ":3306/" + dbName,
                    user, password);

        }catch (Exception e){
            e.printStackTrace();
        }

        return connection;
    }

    public static HashMap<String, Object> getInfoByName(String name){

        HashMap<String, Object> map = new HashMap<>();
        // �������ݿ����ƣ���������
        Connection connection = getConn("map_designer_test_db");

        try {
            // mysql�򵥵Ĳ�ѯ��䡣�����Ǹ���MD_CHARGER���NAME�ֶ�����ѯĳ����¼
            String sql = "select * from MD_CHARGER where NAME = ?";
//            String sql = "select * from MD_CHARGER";
            if (connection != null){// connection��Ϊnull��ʾ�����ݿ⽨��������
                PreparedStatement ps = connection.prepareStatement(sql);
                if (ps != null){
                    // ���������sql����еģ���ֵΪname
                    ps.setString(1, name);
                    // ִ��sql��ѯ��䲢���ؽ����
                    ResultSet rs = ps.executeQuery();
                    if (rs != null){
                        int count = rs.getMetaData().getColumnCount();
                        Log.e("DBUtils","��������" + count);
                        while (rs.next()){
                            // ע�⣺�±��Ǵ�1��ʼ��
                            for (int i = 1;i <= count;i++){
                                String field = rs.getMetaData().getColumnName(i);
                                map.put(field, rs.getString(field));
                            }
                        }
                        connection.close();
                        ps.close();
                        return  map;
                    }else {
                        return null;
                    }
                }else {
                    return  null;
                }
            }else {
                return  null;
            }
        }catch (Exception e){
            e.printStackTrace();
            Log.e("DBUtils","�쳣��" + e.getMessage());
            return null;
        }

    }

}

