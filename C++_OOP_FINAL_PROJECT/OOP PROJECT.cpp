#include <iostream>
#include <climits>
#include <algorithm>

struct Denomination {
    int value;
    int* count;

    Denomination(int v, int c) : value(v) {
        count = new int(c);
    }

    ~Denomination() {
        delete count;
    }
};

class CashDispenser {
protected:
    Denomination** denoms;
    int denomSize;

public:
    CashDispenser() : denoms(nullptr), denomSize(0) {}

    virtual ~CashDispenser() {
        for (int i = 0; i < denomSize; ++i)
            delete denoms[i];
        delete[] denoms;
    }

    void addDenomination(int value, int count) {
        Denomination** newDenoms = new Denomination*[denomSize + 1];
        for (int i = 0; i < denomSize; ++i)
            newDenoms[i] = denoms[i];
        newDenoms[denomSize] = new Denomination(value, count);
        delete[] denoms;
        denoms = newDenoms;
        ++denomSize;
    }

    void removeDenomination(int value) {
        int index = -1;
        for (int i = 0; i < denomSize; ++i) {
            if (denoms[i]->value == value) {
                index = i;
                break;
            }
        }
        if (index == -1) return;

        Denomination** newDenoms = new Denomination*[denomSize - 1];
        for (int i = 0, j = 0; i < denomSize; ++i) {
            if (i != index) newDenoms[j++] = denoms[i];
            else delete denoms[i];
        }
        delete[] denoms;
        denoms = newDenoms;
        --denomSize;
    }

    virtual bool dispense(int amount) = 0;

    void printDenoms() {
        std::cout << "Denominations:\n";
        for (int i = 0; i < denomSize; ++i) {
            std::cout << denoms[i]->value << ": " << *(denoms[i]->count) << " notes\n";
        }
        std::cout << "---------------------\n";
    }
};

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
            *(denoms[i]->count) -= usable;
        }

        return amount == 0;
    }
};

class DPDispenser : public CashDispenser {
public:
    bool dispense(int amount) override {
        int* dp = new int[amount + 1];
        int* lastUsed = new int[amount + 1];
        std::fill(dp, dp + amount + 1, INT_MAX);
        std::fill(lastUsed, lastUsed + amount + 1, -1);
        dp[0] = 0;

        for (int i = 0; i < denomSize; ++i) {
            int val = denoms[i]->value;
            int cnt = *(denoms[i]->count);
            for (int k = 0; k < cnt; ++k) {
                for (int j = amount; j >= val; --j) {
                    if (dp[j - val] != INT_MAX && dp[j - val] + 1 < dp[j]) {
                        dp[j] = dp[j - val] + 1;
                        lastUsed[j] = i;
                    }
                }
            }
        }

        if (dp[amount] == INT_MAX) {
            delete[] dp;
            delete[] lastUsed;
            return false;
        }

        int temp = amount;
        while (temp > 0) {
            int idx = lastUsed[temp];
            if (idx == -1) break;
            *(denoms[idx]->count) -= 1;
            temp -= denoms[idx]->value;
        }

        delete[] dp;
        delete[] lastUsed;
        return true;
    }
};

int main() {
    CashDispenser** machines = new CashDispenser*[2];
    machines[0] = new GreedyDispenser();
    machines[1] = new DPDispenser();

    for (int i = 0; i < 2; ++i) {
        machines[i]->addDenomination(100, 5);
        machines[i]->addDenomination(50, 10);
        machines[i]->addDenomination(20, 10);
        machines[i]->addDenomination(10, 10);
    }

    std::cout << "=== Greedy Dispenser ===\n";
    bool gRes = machines[0]->dispense(180);
    std::cout << "Dispense 180: " << (gRes ? "Success" : "Fail") << "\n";
    machines[0]->printDenoms();

    std::cout << "\n=== DP Dispenser ===\n";
    bool dRes = machines[1]->dispense(180);
    std::cout << "Dispense 180: " << (dRes ? "Success" : "Fail") << "\n";
    machines[1]->printDenoms();

    for (int i = 0; i < 2; ++i)
        delete machines[i];
    delete[] machines;

    return 0;
}

