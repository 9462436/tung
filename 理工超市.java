import java.util.Scanner;
public class a{
    public static void main(String[] args){
        Scanner input=new Scanner(System.in);
        boolean isregister=false;
        String[]goodsName=new String[50];
        double []price=new double[50];
        int []count=new int[50];
        String []newgoodsName=new String[10];
        double []newprice=new double[10];
        int []newcount=new int[10];
        int y=0;
        goodsName[0]="缤纷多味糖果";
        price[0]=3.0;
        count[0]=100;
        goodsName[1]="五彩纸屑气球";
        price[1]=1.5;
        count[1]=50;
        goodsName[2]="亲子装斗篷";
        price[2]=25.0;
        count[2]=50;
        goodsName[3]="晨光中性笔";
        price[3]=1.5;
        count[3]=100;
        while(true){
            System.out.println("************欢迎来到理工超市管理系统************");
            System.out.println("   1.用户注册 2.用户登录 3.浏览商品 4.查看商品");
            System.out.println("   5.加入购物车 6.查看购物车 7.结算 0.退出系统");
            System.out.println("********************************************");
            int choice=input.nextInt();
            switch(choice) {
                case 1:
                    if (signup() == 1)
                        isregister = true;
                    break;
                case 2:
                    if (!isregister)
                        System.out.println("您尚未注册账号，请先注册。");
                    else
                        login();
                    break;
                case 3:
                    System.out.println("编号" + "\t" + "商品名称" + "\t\t" + "单价" + "\t" + "数量");
                    for (int i = 0; i < 4; i++)
                        System.out.println(i + 1 + "\t" + goodsName[i] + "\t" + price[i] + " " + count[i]);
                    break;
                case 4:
                    System.out.println("正在查看商品，请输入需要查看的商品的编号：");
                    int Choice = input.nextInt();
                    while (true) {
                        int k;
                        if (Choice >= 1 && Choice <= 4) {
                            System.out.println("编号" + "\t" + "商品名称" + "\t\t" + "单价" + "\t" + "数量");
                            System.out.println(Choice + "\t" + goodsName[Choice - 1] + "\t" + price[Choice - 1] + " " + count[Choice - 1]);
                            System.out.println("是否继续查看商品？1-YES 2-NO");
                            k = input.nextInt();
                            if (k == 1) {
                                System.out.println("请输入商品编号：");
                                Choice = input.nextInt();
                            } else {
                                System.out.println("欢迎下次光临！");
                                break;
                            }
                        } else {
                            System.out.println("抱歉您所查看的商品不存在。");
                            System.out.println("是否继续查看其它商品？1-YES 2-NO");
                            k = input.nextInt();

                            if (k == 1) {
                                System.out.println("请输入商品编号：");
                                Choice = input.nextInt();
                            } else
                                System.out.println("欢迎下次光临！");
                        }
                    }
                    break;
                case 5:
                    int n, x;
                    System.out.println("请选择您喜欢的商品：");
                    System.out.println("1-缤纷多味糖果 2-五彩纸屑气球 3-亲子装斗篷 4-晨光中性笔");
                    int m = input.nextInt();
                    if (m >= 1 && m <= 4)
                        while (true) {
                            System.out.println("是否将此商品加入购物车？1-YES 2-NO");
                            n = input.nextInt();
                            if (n == 1) {
                                System.out.println("请输入您的购买数量：");
                                newcount[y] = input.nextInt();
                                newgoodsName[y] = goodsName[m - 1];
                                newprice[y] = price[m - 1];
                                System.out.println("添加成功！是否继续购物？");
                                y++;
                                System.out.println("1-YES 2-NO");
                                x = input.nextInt();
                                if (x == 1) {
                                    System.out.println("请重新选择商品的编号：");
                                    m = input.nextInt();
                                }
//                                } else{
//
//                                    System.out.println("编号" + "\t" + "商品名称" + "\t\t" + "单价" + "\t" + "数量");
//                                    for (int i = 0; i < min(4,y); i++)
//                                        System.out.println(i + 1 + "\t" + newgoodsName[i] + "\t" + price[i] + "\t" + newcount[i]);
//                                break;}
//                            }
//                            else {
//                                System.out.println("您的购物车如下（最多展示前四项）:");
//                                System.out.println("编号" + "\t" + "商品名称" + "\t\t" + "单价" + "\t" + "数量");
//                                for (int i = 0; i < min(4,y); i++)
//                                    System.out.println(i + 1 + "\t" + newgoodsName[i] + "\t" + price[i] + "\t" + newcount[i]);
//                                break;
//                            }
//                        }
                                else{
                                    System.out.println("欢迎下次光临！");
                                    break;
                                }
                            }
                        }
                    else {
                        System.out.println("抱歉该商品不在您的购物车内,是否重新选择？1-YES 2-NO");
                        x = input.nextInt();
                        if (x == 1) {
                            System.out.println("请重新选择商品的编号：");
                            m = input.nextInt();
                        } else {
                            System.out.println("欢迎下次光临！");
                            break;
                        }
                    }
                    break;
                case 6:
                    System.out.println("您的购物车如下（最多展示前四项）:");
                    System.out.println("编号" + "\t" + "商品名称" + "\t\t" + "单价" + "\t" + "数量");
                    for (int i = 0; i < min(4, y); i++)
                        System.out.println(i + 1 + "\t" + newgoodsName[i] + "\t" + price[i] + " " + newcount[i]);
                    break;
                case 7:
                    System.out.println("您的购物信息如下，是否需要进行更改？");
                    System.out.println("1-YES 2-NO");
                    System.out.println("编号" + "\t" + "商品名称" + "\t\t" + "单价" + "\t" + "数量");
                    for (int i = 0; i < min(4, y); i++)
                        System.out.println(i + 1 + "\t" + newgoodsName[i] + "\t" + price[i] + " " + newcount[i]);
                    x=input.nextInt();
                    int sum=0;
                    if(x==2) {
                        for(int i=0;i<min(4,y);i++)
                            sum+=newcount[i]*newprice[i];
                        System.out.println("您所需支付的金额为："+sum);
                    }
                    else {

                        int p = 0;
                        do {
                            System.out.println("请输入您需要修改的商品的编号：");
                            x = input.nextInt();
                            System.out.println("更改1-商品，还是2-商品数量？");
                            m = input.nextInt();
                            if (m == 1) {
                                System.out.println("请输入您想要替换商品的编号：1-缤纷多味糖果 2-五彩纸屑气球 3-亲子装斗篷 4-晨光中性笔");
                                n = input.nextInt();
                                newgoodsName[x] = goodsName[n];
                                System.out.println("您是否需要更改此商品数量？1-YES 2-NO");
                                p = input.nextInt();
                                if (p == 1) {
                                    System.out.println("请您输入数量：");
                                    n = input.nextInt();
                                    newcount[x] = n;
                                    System.out.println("更改成功！");
                                } else
                                    break;
                            } else {
                                System.out.println("请您输入数量：");
                                n = input.nextInt();
                                newcount[x] = n;
                                System.out.println("更改成功！");
                            }
                            System.out.println("您是否还需要进行更改？1-YES 2-NO");
                            p = input.nextInt();
                        }while(p!=2);
                        for(int i=0;i<min(4,y);i++)
                            sum+=newcount[i]*newprice[i];
                        System.out.println("您所需支付的金额为："+sum);
                    }
                    break;
                case 0:
                    System.out.println("欢迎下次光临！");
                    return;
            }
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
    public static int min(int a,int b){
        if(a<b)
            return a;
        else
            return b;
    }
}
