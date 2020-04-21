
#include <cassert>

#include <fstream>
#include <sstream>
#include <iostream>
#include <string>

using namespace std;

void Convert(const std::string &file){
    ifstream input_file;
    input_file.open(file);
    assert(input_file.is_open());


    string content, line;

    while (getline(input_file, line)){
        if (*(line.end() -1) == '\r'){
            line.erase(line.end()-1);
        }
        content += line + "\n";
    }

    input_file.close();

    ofstream out_file;
    out_file.open(file);
    assert(out_file.is_open());

    out_file << content << endl;
    
    

}


int main(int argc, char **argv){
    if (argc == 2){
        Convert(argv[1]);
    }else{
        cout << "Useage : crlf2lf file";
    }

    return 0;
}