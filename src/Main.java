import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        List<String> command = new ArrayList<>();
        command.add("python");
        command.add("C:\\Users\\NirmalaDeviKaliappan\\Desktop\\TestPython\\chromeDownload.py");

        ProcessBuilder processBuilder = new ProcessBuilder(command);

        try {

            Process process = processBuilder.start();

            BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));
            String line;
            System.out.println("reading python code");
            while ((line = reader.readLine()) != null) {
                System.out.println(line);
            }


            BufferedReader errorReader = new BufferedReader(new InputStreamReader(process.getErrorStream()));
            while ((line = errorReader.readLine()) != null) {
                System.err.println(line);
            }

           int exitCode = process.waitFor();
            System.out.println("Exited with code: " + exitCode);

        } catch (IOException | InterruptedException e) {
            e.printStackTrace();
        }
    }
}
