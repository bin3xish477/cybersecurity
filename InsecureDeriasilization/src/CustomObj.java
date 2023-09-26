import java.io.IOException;
import java.io.Serializable;

public class CustomObj implements Serializable {
    public static void payload() {
        try {
            Runtime.getRuntime().exec("calc.exe");
        } catch (IOException e) {
        }
    }
}
