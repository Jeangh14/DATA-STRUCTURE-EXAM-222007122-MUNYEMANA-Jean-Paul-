#include <iostream>     // for input/output (e.g., cout)
#include <climits>      // for INT_MAX (used in DP to represent infinity)
#include <algorithm>    // for std::swap, std::min, std::fill
struct Denomination {
 int value;          // The value of the note (e.g., 100, 50)
 int* count;         // Pointer to number of notes of this denomination
 Denomination(int v, int c) : value(v) {
 count = new int(c); // Dynamically allocate memory for coun ~Denomination 
 delete count;       // Free memory to prevent leak
 
class CashDispenser {
protected:
    Denomination** denoms; // Pointer to an array of pointers to Denomination objects
    int denomSize;         // Number of denominations stored
     virtual ~CashDispenser() {
        for (int i = 0; i < denomSize; ++i)
            delete denoms[i];     // Delete each Denomination
        delete[] denoms;          // Delete the array itself
    
    void addDenomination(int value, int count) {
        Denomination** newDenoms = new Denomination*[denomSize + 1]; // New array with 1 extra slot
        for (int i = 0; i < denomSize; ++i)
            newDenoms[i] = denoms[i];  // Copy old pointers
        newDenoms[denomSize] = new Denomination(value, count); // Add new one
        delete[] denoms;
        denoms = newDenoms;
        ++denomSize;

    void removeDenomination(int value) {
        int index = -1;
        for (int i = 0; i < denomSize; ++i) {
            if (denoms[i]->value == value) {
                index = i;
                break
        if (index == -1) return; // If not found
        Denomination** newDenoms = new Denomination*[denomSize - 1];
        for (int i = 0, j = 0; i < denomSize; ++i) {
            if (i != index) newDenoms[j++] = denoms[i]; // Keep others
            else delete denoms[i]; // Delete the one being removed
        
        delete[] denoms;
        denoms = newDenoms;
        --denomSize;
   
    virtual bool dispense(int amount) = 0; // Must be implemented by child classes
    void printDenoms() {
        std::cout << "Denominations:\n";
        for (int i = 0; i < denomSize; ++i) {
            std::cout << denoms[i]->value << ": " << *(denoms[i]->count) << " notes\n";
    
        std::cout << "---------------------\n";

class GreedyDispenser : public CashDispenser {
public:
    bool dispense(int amount) override {
        for (int i = 0; i < denomSize - 1; ++i)
            for (int j = i + 1; j < denomSize; ++j)
                if (denoms[i]->value < denoms[j]->value)
                    std::swap(denoms[i], denoms[j]);
        for (int i = 0; i < denomSize; ++i) {
            int usable = std::min(amount / denoms[i]->value, *(denoms[i]->count));
            amount -= usable * denoms[i]->value;
            *(denoms[i]->count) -= usable
        return amount == 0;
  
       

