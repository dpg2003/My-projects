
#include "stack.h"
#include "eval_expr.h"
#include <cmath>
#include <iostream>
using namespace std;

bool evalPostfixExpr(string postfix_expr, float &result) {
    Stack <float> stack;

    for(int i=0;i<postfix_expr.size();i++){
        if(postfix_expr[i] >= '0' && postfix_expr[i] <= '9'){
            stack.push(postfix_expr[i]-'0');
        }
        else if (postfix_expr[i] =='+'||postfix_expr[i] =='-'||postfix_expr[i] =='*'||postfix_expr[i] =='/'){
            if(i==0|| stack.size()<2){
                cout<<"Error: invalid expression!"<<endl;
                return false;
            }
            float val1=stack.top();
            stack.pop(val1);
            float val2=stack.top();
            stack.pop(val2);

            switch(postfix_expr[i]){
                case '+':
                    stack.push(val2+val1);
                    break;
                case '-':
                    stack.push(val2-val1);
                    break;
                case '*':
                    stack.push(val2*val1);
                    break;
                case '/':
                    if(val1==0){
                        cout<<"Error: division by zero"<<endl;
                        return false;
                    }else{
                        stack.push(val2/val1);
                    }
                    break;
            }
        }else{
            cout<<"Error: unknown symbol"<<endl;
            return false;
        }
    }

    if (stack.size()!=1){
        return false;
    }

    result=stack.top();
    return true;
}

int priority (char symbol){
    switch(symbol){
        case '+':
        case '-':
            return 1;
        case '*':
        case '/':
            return 2;
        default:
            return 0;
    }
}

string convertInfixToPostfix(string infix_expr){
    Stack<char> opstack;
    string postfix;
    char symbol;

    for(int i=0;i<infix_expr.size();i++){
        symbol=infix_expr[i];
        switch(symbol){
            case '(':
                opstack.push(symbol);
                break;
            case ')':
                while (!opstack.isEmpty() && opstack.top() != '(') {
                    postfix += opstack.top();
                    opstack.pop(symbol);
                }
                if (!opstack.isEmpty()) {
                    opstack.pop(symbol);
                }
                break;
            case '+':
            case '-':
            case '*':
            case '/':
                while (!opstack.isEmpty() && priority(opstack.top()) >= priority(symbol)){
                    postfix += opstack.top();
                    opstack.pop(symbol);
                }
                opstack.push(symbol);
                break;
            case '&':
            case '@':
                cout<<"Error: Invalid character "<<symbol<<endl;
                return "";
                break;
            default:
                postfix+=symbol;
                break;
        }
    }
    while (!opstack.isEmpty()) {
        postfix += opstack.top();
        opstack.pop(symbol);
    }
    return postfix;
}
