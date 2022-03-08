import java.nio.charset.StandardCharsets;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.Random;
import java.util.random.*;
public class Customer {
    private String name;
    private String pwd;
    private String salt;
    private char[]hex={'0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F'};
    private String getSalt(){
        Random random=new Random();
        StringBuilder sb=new StringBuilder(16);
        for(int i=0;i<sb.capacity();i++)
            sb.append(hex[random.nextInt(16)]);
        return sb.toString();
    }
    private String getPwdWidthSalt(String pwd,String salt){
        String hashResult=pwd;
        MessageDigest md=null;
        try {
             md = MessageDigest.getInstance("MD5");
        }catch (NoSuchAlgorithmException e){
            e.printStackTrace();
            return hashResult;
        }
        String inputWidthSalt=pwd+salt;
        hashResult=byte2HexStr(md.digest(inputWidthSalt.getBytes()));
        return hashResult;
    }
    private String byte2HexStr(byte[]bytes){
        int len=bytes.length;
        StringBuffer result=new StringBuffer();
        for(int i=0;i<len;i++){
            byte byte0=bytes[i];
            result.append(hex[byte0>>>4&0xf]);
            result.append(hex[byte0&0xf]);
        }
        return result.toString();
    }
    public Customer(String name,String pwd){
        this.name=name;
        this.salt=getSalt();
        this.pwd=getPwdWidthSalt(pwd,this.salt);
    }
    public boolean loginValidate(String name,String pwd){
        boolean isregister=false;
        String userPwd=getPwdWidthSalt(pwd,this.salt);
        if(this.name.equals(name)&&this.pwd.equals(userPwd)){
            isregister=true;
        }
        return isregister;
    }
}
