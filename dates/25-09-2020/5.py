aws eks update-kubeconfig --name eks-test --region us-east-1

aws-iam-authenticator token -i eks-test

kubectl edit cm/aws-auth -n kube-system



