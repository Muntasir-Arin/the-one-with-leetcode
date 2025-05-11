func threeConsecutiveOdds(arr []int) bool {
	var pat strings.Builder
    for _,num:=range arr{
        if num%2==1{
            pat.WriteByte('O')
        }else{
            pat.WriteByte('E')
        }
    }
    return strings.Contains(pat.String(),"OOO")
}