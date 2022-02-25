import java.util.Scanner;
public class a{
    public static void main(String[] args){
        Scanner input=new Scanner(System.in);
        boolean isregister=false;

        while(true){
            System.out.println("************欢迎来到理工超市管理系统************");
            System.out.println("   1.用户注册 2.用户登录 3.浏览商品 4.查看商品");
            System.out.println("   5.加入购物车 6.查看购物车 7.结算 0.退出系统");
            System.out.println("*******************************************");
            int choice=input.nextInt();


            switch(choice){

                case 1:
                   if(signup()==1)
                       isregister=true;
                    break;
                case 2:
                    if(!isregister)
                        System.out.println("您尚未注册账号，请先注册。");
                    else
                        login();
                    break;
                case 3:
                    break;
                case 4:
                    break;
                case 5:
                    break;
                case 6:
                    break;
                case 7:
                    break;
                case 0:
                    System.out.println("欢迎下次光临！");
                    break;
            }
            if(choice==0)
                break;
        }


    }
    public static void login(){
        int random=(int)(Math.random()*9000)+1000;
        Scanner input=new Scanner(System.in);
        System.out.println("请输入用户名：");
        String username=input.next();
        while(!"123".equals(username)) {
            System.out.println("对不起，用户名错误。请再次输入：");
            username=input.next();
        }
        System.out.println("请输入密码：");
        String pwd=input.next();
        while(!"123".equals(pwd)) {
            System.out.println("对不起，密码错误。");
            pwd=input.next();
        }
        System.out.println("请输入验证码："+random);
        int number=input.nextInt();
        System.out.println("登录成功！");
    }
    public static int signup(){
        int m=0;
        int random=(int)(Math.random()*9000)+1000;
        Scanner input=new Scanner(System.in);
        System.out.println("正在进行用户注册，请输入下列信息。");
        System.out.println("请输入用户名：");
        String username=input.next();
        System.out.println("请输入密码：");
        String pwd1=input.next();
        System.out.println("请再次输入密码：");
        String pwd2=input.next();
        while(!pwd2.equals(pwd1)){
            System.out.println("对不起，密码不一致，请再次输入密码：");
            pwd2=input.next();
        }
        System.out.println("请输入验证码：" + random);
        int number = input.nextInt();
        if (number != random)
            System.out.println("验证码错误，请再次输入。");
        else {
            System.out.println("恭喜您注册成功！");
            m++;
        }
        return m;
    }
}
