using System;
using System.IO;
using System.Security.Cryptography;
//using System.Text;

namespace CSharpAES
{
    class Encryptor
    {
        static int Main(string[] args)
        {
            try
            {
                // if no arguments were passed to program
                if(args.Length == 0)
                {
                    Console.WriteLine("Usage: encryptor.exe [fileName]");
                    return 1;
                }
                // get file to encrypt
                string fileToEncrypt = args[0];
                string encryptedFileName = $"{fileToEncrypt}.encrypted";
                // check if specified file exists
                if(!File.Exists(fileToEncrypt))
                {
                    Console.WriteLine($"The file {fileToEncrypt} does not exist...");
                    return 1;
                }
                // if encrypted file already exists, delete it
                if(File.Exists(encryptedFileName))
                    File.Delete(encryptedFileName);
                // read all data from the original file as one string
                string fileContents = File.ReadAllText(fileToEncrypt);
                // creating file stream for encryption 
                FileStream fStream = new FileStream(encryptedFileName, FileMode.Create);
                // invoke function to generate key and iv for encryption
                var keyIVPair = GenerateKeyAndIv(16, 16);
                // creating AES encryption object
                Aes aes = Aes.Create();
                // set aes object block size to 128 (16 bytes)
                aes.BlockSize = 128;
                // creating a cryptostream to encrypt filestream using an aes object
                CryptoStream cryptoStream = new CryptoStream(
                    fStream,
                    aes.CreateEncryptor(keyIVPair.Item1, keyIVPair.Item2),
                    CryptoStreamMode.Write
                );
                // creating a stream writer to easily write to the file stream
                StreamWriter streamWriter = new StreamWriter(cryptoStream);
                // writing encrypted data back into original file
                streamWriter.WriteLine(fileContents);

                streamWriter.Close();
                cryptoStream.Close();
                fStream.Close();
                Console.WriteLine(
                    $"The encrypted file contents can be found in the file: '{encryptedFileName}'"
                );
            }
            catch (UnauthorizedAccessException)
            {
                Console.WriteLine("Unable to access file... permission denied");
                return 1;
            }
            return 0;
        }

        public static Tuple<byte[], byte[]> GenerateKeyAndIv(sbyte keySize, sbyte IVSize)
        {
            // creating Random object for generating random bytes
            Random rnd = new Random();
            // creating byte array for encryption key
            byte[] key = new byte[keySize];
            // creating byte array for initialization vector 
            byte[] iv = new byte[IVSize];
            // fill key and iv byte arrays with random bytes 
            rnd.NextBytes(key);
            rnd.NextBytes(iv);

            //string KeyString = Encoding.Default.GetString(key);
            //string IVString = Encoding.Default.GetString(iv);

            //Console.WriteLine($"Key = {KeyString}");
            //Console.WriteLine($"IV = {IVString}");
            return new Tuple<byte[], byte[]>(key, iv);
        }
    }
}
