using MathNet.Numerics.LinearAlgebra;

namespace Connect4;

class Game
{

    private static int lastColumn_Int = 0;

    private static int player1_Int = 1;

    private static int player2_Int = 2;

    private static bool botFirst_Bool = false;

    private static bool singlePlayer_Bool = true;

    private static string error_String = "";

    private static string botInfo_String = "";
    
    private static void SideSelect_Function()
    {

        bool pointer_Bool = false;

        string singlePlayer_String = "";

        if(!singlePlayer_Bool)
            singlePlayer_String = "First Player, ";

        while(!MyUI.UserInterface_Function($"{singlePlayer_String}Select Your Side (Use Up/Down Arrow Keys, Escape To Exit):", "O", "X", pointer_Bool,out bool valid_Bool, out bool exit_Bool))
        {

            if(exit_Bool)
                PrematureExit_Function();

            if(valid_Bool)
                (player1_Int, player2_Int,pointer_Bool) = (player2_Int, player1_Int,!pointer_Bool);

        }

        pointer_Bool = false;

        if(singlePlayer_Bool)
            while(!MyUI.UserInterface_Function("Who Goes First? (Use Up/Down Arrow Keys, Escape To Exit):", "You", "Bot", pointer_Bool,out bool valid_Bool, out bool exit_Bool))
            {

                if(exit_Bool)
                    PrematureExit_Function();

                if(valid_Bool)
                    (botFirst_Bool, pointer_Bool) = (!botFirst_Bool, !pointer_Bool);

            }

    }

    private static void GameMode_Function()
    {

        bool pointer_Bool = false;

        while(!MyUI.UserInterface_Function("Select Game Mode (Use Up/Down Arrow Keys, Escape To Exit):", "PvE (Single Player)", "PvP (Couch Play)", pointer_Bool,out bool valid_Bool, out bool exit_Bool))
        {

            if(exit_Bool)
                PrematureExit_Function();

            if(valid_Bool)
                (singlePlayer_Bool, pointer_Bool) = (!singlePlayer_Bool, !pointer_Bool);

        }

    }

    private static void BotDifficulty_Function()
    {

        bool pointer_Bool = false;

        bool botDifficulty_Bool = false;

        bool dumbBot_Bool = false;

        while (!MyUI.UserInterface_Function($"Select Opponent Type:", "Normal", "Advanced", pointer_Bool, out bool valid_Bool, out bool exit_Bool))
        {            

            if (exit_Bool) Game.PrematureExit_Function();

            if(valid_Bool)
                (botDifficulty_Bool,pointer_Bool) = (!botDifficulty_Bool,!pointer_Bool);

        }

        pointer_Bool = false;

        while (!MyUI.UserInterface_Function($"Enable Clumsy Bot? (Bot Might Get Dumb)", "No", "Yes", pointer_Bool, out bool valid_Bool, out bool exit_Bool))
        {            

            if (exit_Bool) Game.PrematureExit_Function();

            if(valid_Bool)
                (dumbBot_Bool,pointer_Bool) = (!dumbBot_Bool,!pointer_Bool);

        }

        botInfo_String = Bot.BotSet_Function(botDifficulty_Bool, dumbBot_Bool,player1_Int, player2_Int);
    
    }

    public static void Load_Function()
    {

        lastColumn_Int = 0;

        player1_Int = 1;

        player2_Int = 2;

        botFirst_Bool = false;

        singlePlayer_Bool = true;

        error_String = "";

        botInfo_String = "";

        // string loading_String = "[                    ]";        

        // bool loading_Bool = true;

        // for (int loading_Int = 2; loading_Int < 23; loading_Int++)
        // {            

        //     Console.Clear();            

        //     System.Console.Write("Loading");

        //     System.Console.Write(loading_String);

        //     if(loading_Int == 22)System.Console.WriteLine("100%");
        //     else System.Console.WriteLine((int)((double)loading_Int/23*100)+"%");

        //     loading_String = loading_String[..(loading_Int-1)] + "-" + loading_String[(loading_Int)..];

        //     if(loading_Int == 4)Thread.Sleep(200);

        //     if(loading_Bool)
        //     {

        //         if(loading_Int%1==0)Thread.Sleep(1);

        //         if(loading_Int%3==0)Thread.Sleep(30);

        //         if(loading_Int%5==0)Thread.Sleep(100);

        //         if(loading_Int%6==0)Thread.Sleep(200);

        //         if(loading_Int%7==0)Thread.Sleep(300);

        //         if(loading_Int%10==0)
        //         {

        //             Thread.Sleep(400);

        //             loading_Bool = false;

        //         }

        //     }else Thread.Sleep(5);

        // }

        // for (int loading_Int = 3; loading_Int > 0; loading_Int--)
        // {

        //     System.Console.WriteLine("Game Starting In " + loading_Int + "...");

        //     Thread.Sleep(900);

        // }

        // Thread.Sleep(200);

        Console.Clear();

        GameMode_Function();

        if(singlePlayer_Bool)
            BotDifficulty_Function();

        SideSelect_Function();

        Game_Function();

    }

    private static void Game_Function()
    {

        GameBoard.GameBoardReset_Function();
    
        error_String = "";

        if(singlePlayer_Bool)
            while (true)
            {

                if(botFirst_Bool)
                    Action_Function(Bot.Bot_Function(), player2_Int);
                else if(!PlayerTurn_Function(player1_Int))
                    break;
                
                if(CheckGoal_Function())
                    break;

                if(botFirst_Bool)
                {

                    if(!PlayerTurn_Function(player1_Int))
                        break;

                }else
                    Action_Function(Bot.Bot_Function(), player2_Int);

                if(CheckGoal_Function())
                    break;

            }
        else
            while (true)
            {

                if(!PlayerTurn_Function(player1_Int))
                    break;
                
                if(CheckGoal_Function())
                    break;

                if(!PlayerTurn_Function(player2_Int))
                    break;

                if(CheckGoal_Function())
                    break;

            }
    
    }

    private static bool PlayerTurn_Function(int player_Int)
    {

        while (true)
        {

            int elementColumn_Int = MyUI.GameInterface_Function(error_String, GameBoard.GameBoardStatus_Function(), player_Int, lastColumn_Int,botInfo_String);

            error_String = "";

            lastColumn_Int = elementColumn_Int;

            if(elementColumn_Int == -1)
                PrematureExit_Function();

            if(elementColumn_Int == -2)
                return false;

            if(Action_Function(elementColumn_Int, player_Int))
                return true;

            error_String = $"Can't Place There (Column: {elementColumn_Int + 1})";

        }

    }

    private static bool Action_Function(int elementColumn_Int, int ID_Int)
    {
        
        if(GameBoard.ElementValidColumn_Function(
            GameBoard.GameBoardStatus_Function(), elementColumn_Int, out int elementRow_Int ))
            if(GameBoard.ElementPlace_Function(elementRow_Int, elementColumn_Int, ID_Int))
                return true;

        return false;
    
    }
    
    private static bool CheckGoal_Function()
    {

        int winner_int = -1;

        for (int corner_Int = 1; corner_Int < 5; corner_Int++)
        {

            if(winner_int == player2_Int | winner_int == player1_Int)
                break;

            GameBoard.SubMatrix_Function(GameBoard.GameBoardStatus_Function(),
                corner_Int, out Matrix<float> fourByFour_SingleMatrix);

            Matrix<float> mirror_SingleMatrix = Matrix<float>.Build.Dense(4,4,0);

            for (int i = 0; i < 4; i++)
            {

                mirror_SingleMatrix[3-i,i] = 1;
                
            }

            for (int ID_Int = 1; ID_Int < 3; ID_Int++)
            {

                if(winner_int == player2_Int | winner_int == player1_Int)
                    break;

                if(fourByFour_SingleMatrix.Diagonal().ToList().All(x => x == ID_Int))
                {

                    winner_int = ID_Int;

                    break;

                }

                if(fourByFour_SingleMatrix.Multiply(mirror_SingleMatrix).Diagonal().ToList().All(x => x == ID_Int))
                {

                    winner_int = ID_Int;

                    break;

                }

                for (int index_Int = 0; index_Int < 4; index_Int++)
                {

                    if(fourByFour_SingleMatrix.Row(index_Int).ToList().All(x => x == ID_Int))
                    {

                        winner_int = ID_Int;

                        break;

                    }

                    if(fourByFour_SingleMatrix.Column(index_Int).ToList().All(x => x == ID_Int))
                    {

                        winner_int = ID_Int;

                        break;

                    }
                    
                }

            }

        }

        if(winner_int == -1 & GameBoard.GameBoardStatus_Function().Find(x => x == 0) == null)
        {

            Console.Clear();
            
            System.Console.Write("Tied, Game Over!");

            MyUI.ShowMenu_Function(GameBoard.GameBoardStatus_Function(), -1);

            System.Console.WriteLine("Press Anything To Continue");

            Console.ReadKey();

            return true;

        }

        if(winner_int == player1_Int)
        {

            string player_String = "";

            Console.Clear();

            if(singlePlayer_Bool)
                player_String = "You Won!";
            else
                player_String = "Player 1 Won!";
            
            System.Console.Write(player_String);

            MyUI.ShowMenu_Function(GameBoard.GameBoardStatus_Function(), -1);

            System.Console.WriteLine("Press Anything To Continue");

            Console.ReadKey();

            return true;
            
        }

        if(winner_int == player2_Int)
        {

            string player_String = "";

            Console.Clear();

            if(singlePlayer_Bool)
                player_String = "You Lost, Better Luck Next Time!";
            else
                player_String = "Player 2 Won!";
            
            System.Console.Write(player_String);

            System.Console.Write("You Lost, Better Luck Next Time!");

            MyUI.ShowMenu_Function(GameBoard.GameBoardStatus_Function(), -1);

            System.Console.WriteLine("Press Anything To Continue");

            Console.ReadKey();

            return true;
        
        }

        return false;

    }

    public static bool Rematch_Function()
    {

        bool option_Bool = false;

        bool pointer_Bool = false;

        while(!MyUI.UserInterface_Function("Rematch? (Use Up/Down Arrow Keys, Escape To Exit)", "No", "Yes", pointer_Bool,out bool valid_Bool, out bool exit_Bool))
        {

            if(exit_Bool)
                PrematureExit_Function();

            if(valid_Bool)
                (option_Bool,pointer_Bool) = (!option_Bool,!pointer_Bool);

        }

        return option_Bool;

    }

    private static void PrematureExit_Function()
    {

        Console.Clear();

        System.Console.WriteLine("Have A Nice Day!");

        Thread.Sleep(300);

        Environment.Exit(0);

    }

}