{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "8fb783b0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']\n",
      "['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya', 'kiwi', 'orange']\n",
      "['apple', 'cherry', 'mango', 'pineapple', 'papaya', 'kiwi', 'orange']\n",
      "['apple', 'orange', 'banana', 'cherry', 'kiwi']\n",
      "['apple', 'banana', 'cherry', 'kiwi']\n",
      "['apple', 'banana', 'cherry']\n",
      "['apple', 'cherry']\n",
      "['apple', 'orange', 'banana', 'cherry', 'kiwi']\n",
      "[]\n",
      "apple\n",
      "banana\n",
      "cherry\n",
      "kiwi\n",
      "mango\n",
      "['apple', 'banana', 'mango']\n",
      "[0, 1, 2, 3, 4]\n",
      "['APPLE', 'BANANA', 'CHERRY', 'KIWI', 'MANGO']\n",
      "['hello', 'hello', 'hello', 'hello', 'hello']\n",
      "['apple', 'orange', 'cherry', 'kiwi', 'mango']\n",
      "['banana', 'kiwi', 'mango', 'orange', 'pineapple']\n",
      "['pineapple', 'orange', 'mango', 'kiwi', 'banana']\n"
     ]
    }
   ],
   "source": [
    "#extend() used to append element to current list from another list\n",
    "thislist = [\"apple\", \"banana\", \"cherry\"]\n",
    "tropical = [\"mango\", \"pineapple\", \"papaya\"]\n",
    "thislist.extend(tropical)\n",
    "print(thislist)\n",
    "#print(thislist.extend(tropical))\n",
    "\n",
    "thistuple=(\"kiwi\", \"orange\")\n",
    "thislist.extend(thistuple)\n",
    "print(thislist)\n",
    "thislist.remove(\"banana\")\n",
    "print(thislist)\n",
    "second_list = [\"apple\", \"banana\",\"orange\", \"banana\", \"cherry\", \"kiwi\"]\n",
    "second_list.remove(\"banana\") #default that remove first target in list\n",
    "print(second_list) \n",
    "second_list.pop(1) #delete \"orange\"\n",
    "print(second_list)\n",
    "second_list.pop() #delete last item in list:\"kiwi\"\n",
    "print(second_list)\n",
    "del second_list[1]\n",
    "print(second_list)\n",
    "del second_list\n",
    "del thislist\n",
    "del thistuple\n",
    "\n",
    "#until now, deleted all list, none of available list\n",
    "\n",
    "first_list = [\"apple\", \"orange\", \"banana\", \"cherry\", \"kiwi\"]\n",
    "print(first_list)\n",
    "first_list.clear() \n",
    "print(first_list)\n",
    "\n",
    "#loop list\n",
    "third_list = [\"apple\", \"banana\",\"cherry\",\"kiwi\", \"mango\"]\n",
    "[print(x) for x in third_list]\n",
    "\n",
    "\n",
    "#list comprehension\n",
    "\n",
    "# new_list = []\n",
    "\n",
    "# for x in third_list:\n",
    "#     if \"a\" in x:\n",
    "#         new_list.append(x)\n",
    "\n",
    "new_list = [x for x in third_list if \"a\" in x]\n",
    "print(new_list)\n",
    "new_list = [x for x in range(10) if x < 5] #filter if \n",
    "print(new_list)\n",
    "new_list = [x.upper() for x in third_list]\n",
    "print(new_list)\n",
    "new_list = [\"hello\" for x in third_list]\n",
    "print(new_list)\n",
    "new_list = [x if x != \"banana\" else \"orange\" for x in third_list] #expression\n",
    "print(new_list)\n",
    "\n",
    "#sort list:use sort() method tahtsort the lst alphanumerically ascending \n",
    "#the defualt is ascending and sort(reverse = true) means descending\n",
    "this_list = [\"orange\", \"mango\",\"kiwi\", \"pineapple\", \"banana\"]\n",
    "this_list.sort()\n",
    "print(this_list)\n",
    "\n",
    "this_list.sort(reverse = True)\n",
    "print(this_list)\n",
    "\n",
    "#sort funcrion:it can be customze\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c1666784",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}